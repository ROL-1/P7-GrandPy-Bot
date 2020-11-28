"""Search localisation with Mediawiki API.

In: parsed user question (string).
Act : Use MediaWiki API (external API).
Out : 1 search result, with introduction (json)
"""

import requests

from ..api.apiconfig import wikipedia


class WikiApi:
    """Search a localisation with Mediawiki API."""

    def __init__(self, geo_coord_results):
        """Define parameters to create endpoint.""" 
        self.URL = wikipedia['URL']
        self.geo_coord_results = geo_coord_results


    def get_wikipedia(self,params):
        response =  requests.get(url=self.URL, params=params)
        return response

    @property
    def coordsearch(self):
        """Create and pass request for Wiki Media Api."""
        long = self.geo_coord_results[0]
        lat = self.geo_coord_results[1]
        params = {
            "action": "query",
            "list": "geosearch",
            "gscoord": f"{lat}|{long}",
            "gsradius": 10,
            "gslimit": 1,
            "format": "json"
        }
        response = self.get_wikipedia(params)
        return response
    
    def pageid(self, coordsearch_response):
        """"""
        self.pageid = coordsearch_response.json()['query']['geosearch'][0]['pageid']

    @property
    def pagewiki(self):
        """"""
        params = {
            "pageids": self.pageid,
            "action": "query",            
            "prop":"extracts",
            "explaintext":"1",
            "exintro": "1",
            "format": "json",
            "exsentences": wikipedia['SENTENCES_LIMIT'],
        }
        
        response = self.get_wikipedia(params)
        return response

    def extract(self, pagewiki_response):
        """"""
        self.extract = pagewiki_response.json()['query']['pages'][str(self.pageid)]['extract']
        print(self.extract)


