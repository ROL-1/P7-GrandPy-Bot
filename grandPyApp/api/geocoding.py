"""Search a localisation with Geocoding API.

In : parsed user question (string).
Act : Geocoding API (external API).
Out : 1 search result, with coordinates (json)
"""

import requests

from ..api.apiconfig import geocoding
from ..settings import MAPBOX_API_KEY

class Geocoding:
    """Search a localisation with Geocoding API."""

    def __init__(self, parsed_string):
        """Define parameters to create endpoint."""
        search_terms = parsed_string+'.json?' #"bordeaux" # parsed_string # TC
        self.URL = geocoding['URL']+search_terms
        self.PARAMS = {
            "access_token" : MAPBOX_API_KEY,
            "country" : geocoding['COUNTRY'],
            "limit": geocoding['RESULTS_LIMIT']
        }
        self.response = self.get_geocoding()

    def get_geocoding(self):
        """Create and pass request for Geocoding API (MapBox)."""
        response = requests.get(url=self.URL, params=self.PARAMS)
        return response

    @property
    def coord(self):      
        return  self.response.json()['features'][0]['center']

    @property
    def adress(self):       
        return  self.response.json()['features'][0]['place_name']


