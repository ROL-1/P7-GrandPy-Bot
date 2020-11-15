"""Architecture file for grandPyApp."""

from grandPyApp.parser import Parser
from grandPyApp.geocoding import Geocoding
from grandPyApp.wikipedia import WikiApi

class Main:
    """"""    
    
    def __init__(self, question_send):
        """"""
        self.parsed_string = Parser(question_send).parsed_string
        
        try:
            self.geo_coord_results = Geocoding(self.parsed_string).geocoding_results['features'][0]['center']
        except KeyError as e:
            if e.args[0] == 'features' :
                self.geo_coord_results = 'FAIL' # TC : A GERER ####
            else:
                raise

        try:
            self.geo_adress_results = Geocoding(self.parsed_string).geocoding_results['features'][0]['properties']['address']
        except KeyError as e:
            if e.args[0] == 'address' :
                self.geo_adress_results = 'Adresse inconnue.'
            else:
                raise
        
        try:
            wiki_return = WikiApi(self.parsed_string).wiki_results['query']['pages']
            for k in wiki_return.keys():
                pageid = k
            self.wiki_results = wiki_return[pageid]['extract']
        except KeyError as e:
            if e.args[0] == 'query' :
                self.wiki_results = 'REFORMULEZ !' # TC : A GERER ####
            else:
                raise
        
        
# M = Main("mairie")
# print('##PARSED##',M.parsed_string)
# print('##GEO-COORD##',M.geo_coord_results)
# print('##GEO-ADRESS##',M.geo_adress_results)
# print('##WIKI##',M.wiki_results)