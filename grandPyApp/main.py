"""Architecture file for grandPyApp."""

import json

from .api.geocoding import Geocoding
from .api.wikipedia import WikiApi
from .parser.interpreter import Interpreter
from .parser.parser import Parser
from .parser.reactions import Reactions


class Main:
    """Call modules and adapts responses for sucess or fails."""

    def __init__(self, question_send):
        """Load bot answers from bot_answers.json and call functions."""
        with open(
            "grandPyApp/static/ressources/bot_answers.json",
            "r", encoding="utf-8"
        ) as data:
            self.bot_answers = json.load(data)
        self.main(question_send)

    def main(self, question_send):
        """Launch functions for class : Main."""
        # Clean and parse the question
        self.parse(question_send)
        # Analyse the words selected
        self.interpreter()
        # Launch searches if parsed_string is not empty
        if self.parsed_string != "":
            self.geo()
        else:
            self.geo_failed(self.bot_answers["NO_WORD"])
        # Call wikipedia only if geocoding have not failed
        if self.geo_fail is False:
            self.wiki()

    def geo_failed(self, geo_fail_message):
        """Reaction if geocoding module fail."""
        self.geo_adress_results = geo_fail_message
        self.geo_coord_results = [0, 0]
        # Boolean for css display red border
        self.geo_fail = True
        # MediaWiki is not called
        self.wiki_results = self.bot_answers["FAIL_GEO_WIKI"]
        self.wiki_fail = True

    def wiki_failed(self, wiki_fail_message):
        # MediaWiki is not called
        self.wiki_results = wiki_fail_message
        self.wiki_fail = True

    def parse(self, question_send):
        """Call parse.py.

        In : question_send (string).
        Act : Call parse.py, check result.
        Out : parsed_string (string) : selected words for geocoding.
        """
        self.parsed_string = Parser(question_send).parsed_string

    def interpreter(self):
        """"""
        i = Interpreter(self.parsed_string)
        self.parsed_string = i.better_words
        r = Reactions(i.reactions)
        self.bonus_message = " ".join(r.bonus_message)

    def geo(self):
        """Call geocoding.py to make a request to MediaWiki (Wikipedia) API.

        In : parsed_string (string).
        Act : Call geocoding.py, check result.
        Out : geo_adress_results (string) : sucess or fail message to display;
              geo_coord_results (list) : coordinates for the map.
        """

        #  Call geocoding.py to make a request to Geocoding (Mapbox) API
        g = Geocoding(self.parsed_string)
        # Check if there is a response
        if g.status_code == 200:
            try:
                # Read the response, looking for coordinates
                g_coord = g.coord
                # Check if there is the response is empty
                if g_coord == "":
                    self.geo_failed(self.bot_answers["EMPTY_GEO"])
                else:
                    # Return good response
                    self.geo_coord_results = g_coord
                    try:
                        # Read the response, looking for adress
                        g_adress = g.adress
                        # Check if there is the response is empty
                        if g_adress == "":
                            self.geo_failed(self.bot_answers["EMPTY_GEO"])
                        else:
                            # Return good response
                            self.geo_adress_results = g_adress
                            self.geo_fail = False
                    except (KeyError, IndexError):
                        self.geo_failed(self.bot_answers["UNKNOW_ADRESS"])
            except (KeyError, IndexError):
                self.geo_failed(self.bot_answers["UNKNOW_ADRESS"])
        else:
            if g.status_code == 401:
                self.geo_failed(self.bot_answers["FAIL_GEO_AUTHORIZATION"])
            else:
                self.geo_failed(self.bot_answers["FAIL_GEO"]
                                + str(g.status_code))

    def wiki(self):
        """Call wikipedia.py to make a request to MediaWiki (Wikipedia) API.

        In : parsed_string (string).
        Act : Call wikipedia.py, check result.
        Out : wiki_results (string) : sucess or fail message to display.
        """
        w = WikiApi(self.geo_coord_results)
        try:
            coordsearch = w.coordsearch
            if coordsearch.status_code == 200:
                w.pageid(coordsearch)
                try:
                    pagewiki = w.pagewiki
                    if pagewiki.status_code == 200:
                        w.extract(pagewiki)
                        wiki_results = w.infos
                        # Verify if extract field is empty
                        if wiki_results == "":
                            self.wiki_failed(self.bot_answers["EMPTY_WIKI"])
                        else:
                            # Return good response
                            self.wiki_results = wiki_results
                            self.wiki_fail = False
                    else:
                        self.wiki_failed(self.bot_answers["FAIL_WIKI"])
                except (KeyError, IndexError):
                    self.wiki_failed(self.bot_answers["NO_RESULT"])
            else:
                self.wiki_failed(self.bot_answers["NO_RESULT"])
        except (KeyError, IndexError):
            self.wiki_failed(self.bot_answers["FAIL_WIKI"])
