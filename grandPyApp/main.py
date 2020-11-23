"""Architecture file for grandPyApp."""

import json

from .parser.parser import Parser
from .api.geocoding import Geocoding
from .api.wikipedia import WikiApi
from .parser.interpreter import Interpreter

class Main:
    """Call modules and adapts responses for sucess or fails."""    
    
    def __init__(self, question_send):
        """Load bot answers from bot_answers.json and call functions."""
        with open('grandPyApp/static/ressources/bot_answers.json') as json_data:
            self.bot_answers = json.load(json_data)
        self.main(question_send)        

    def main(self, question_send):
        """Launch functions for class : Main."""
        self.parse(question_send)
        self.interpreter()
        self.geo()
        self.wiki()

    def parse(self, question_send):
        """Call parse.py.

        In : question_send (string).
        Act : Call parse.py, check result.
        Out : parsed_string (string) : selected words for geocoding and wikipedia searches.
        """
        self.parsed_string = Parser(question_send).parsed_string

    def interpreter(self):
        """"""
        i = Interpreter(self.parsed_string)
        print("###i.better_words :",i.better_words)
        self.parsed_string = i.better_words

    def geo(self):
        """Call geocoding.py to make a request to MediaWiki (Wikipedia) API.

        In : parsed_string (string).
        Act : Call geocoding.py, check result.
        Out : geo_adress_results (string) : sucess or fail message to display to user ;
              geo_coord_results (list) : coordinates for the map.
        """
        self.geo_fail = True
        #  Call geocoding.py to make a request to Geocoding (Mapbox) API
        g = Geocoding(self.parsed_string).geocoding_results
        # Check if there is a response
        if g.status_code == 200:
            try:
                print(g.json()['features'])
                # Read the response, looking for coordinates
                g_coord = g.json()['features'][0]['center']
                # Check if there is the response is empty
                if g_coord == '':
                    self.geo_coord_results = [0,0] # TC : A GERER ####
                else:
                    # Return good response
                    self.geo_coord_results = g_coord
            except KeyError as e:
                if e.args[0] == 'features' :
                    self.geo_coord_results = [0,0] # TC : A GERER ####
                else:
                    raise # TC
            except IndexError:           
                self.geo_coord_results = [0,0] # TC : A GERER ####
            try:
                # Read the response, looking for adress
                g_adress = g.json()['features'][0]['place_name']
                # Check if there is the response is empty
                if g_adress == '':
                    self.geo_adress_results = self.bot_answers['BOT_EMPTY_GEO']  # TC : A GERER ####
                else:
                    # Return good response
                    self.geo_adress_results = g_adress
                    self.geo_fail = False
            except KeyError as e:
                if e.args[0] == 'address' :
                    self.geo_adress_results = self.bot_answers['BOT_UNKNOW_ADRESS']
                else:
                    raise # TC
            except IndexError:           
                self.geo_adress_results = self.bot_answers['BOT_UNKNOW_ADRESS']
        else:
            self.geo_adress_results =  self.bot_answers['BOT_FAIL_GEO']+str(g.status_code)
            self.geo_coord_results = [0,0]

    def wiki(self):
        """Call wikipedia.py to make a request to MediaWiki (Wikipedia) API.

        In : parsed_string (string).
        Act : Call wikipedia.py, check result.
        Out : wiki_results (string) : sucess or fail message to display to user.
        """
        self.wiki_fail = True
        #  Call wikipedia.py
        w = WikiApi(self.parsed_string).wiki_results
        # Check if there is a response from 
        if w.status_code == 200:
            try:
                # Read the response, looking for adress
                w_results = w.json()['query']['pages']
                for k in w_results.keys():
                    pageid = k                           
                wiki_results = w_results[pageid]['extract']
                # Check if there is the response is empty
                if wiki_results == '':
                    self.wiki_results =  self.bot_answers['BOT_EMPTY_WIKI']
                else:
                    # Return good response
                    self.wiki_results = wiki_results
                    self.wiki_fail = False
            except KeyError as e:
                if e.args[0] == 'query' :
                    self.wiki_results = self.bot_answers['BOT_NO_RESULT']
                else:
                    raise
            except IndexError:           
                self.wiki_results = self.bot_answers['BOT_NO_RESULT']
        else:
            self.wiki_results =  self.bot_answers['BOT_FAIL_WIKI']+str(w.status_code)
