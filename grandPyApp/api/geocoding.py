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
        self.geocoding_results = self.get_Geocoding()

    def get_Geocoding(self):
        """Create and pass request for Geocoding API (MapBox)."""
        request = requests.get(url=self.URL, params=self.PARAMS)
        return request

    # def adress():