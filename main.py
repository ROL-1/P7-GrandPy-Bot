"""Architecture file for grandPyApp."""

from grandPyApp.parser import Parser
from grandPyApp.geocoding import Geocoding
from grandPyApp.wikipedia import WikiApi

class Main:
    """"""    
    
    def __init__(self, question_send):
        """"""
        self.parsed_string = Parser(question_send).parsed_string
        self.geo_coord_results = Geocoding(self.parsed_string).geocoding_results['features'][0]['center']
        self.geo_adress_results = Geocoding(self.parsed_string).geocoding_results['features'][0]['properties']['address']
        wiki_return = WikiApi(self.parsed_string).wiki_results['query']['pages']
        for k in wiki_return.keys():
            pageid = k
        self.wiki_results = wiki_return[pageid]['extract']
        
        
# M = Main("mairie caen")
# print('##PARSED##',M.parsed_string)
# print('##GEO-COORD##',M.geo_coord_results)
# print('##GEO-ADRESS##',M.geo_adress_results)
# print('##WIKI##',M.wiki_results)