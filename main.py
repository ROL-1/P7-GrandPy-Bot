"""Architecture file for grandPyApp."""

from grandPyApp.parser import Parser
from grandPyApp.geocoding import Geocoding
from grandPyApp.wikipedia import WikiApi

class Main:
    """"""    
    
    def __init__(self, question_send):
        """"""
        self.parsed_string = Parser(question_send).parsed_string
        self.geocoding_results = Geocoding(self.parsed_string).geocoding_results['features'][0]['center']
        wiki_return = WikiApi(self.parsed_string).wiki_results['query']['pages']
        for k in wiki_return.keys():
            pageid = k
        self.wiki_results = wiki_return[pageid]['extract']
        
        
# a = Main("Paris")
# print('##PARSED##',a.parsed_string)
# print('##GEO##',a.geocoding_results[0])
# print('##WIKI##',a.wiki_results)