"""Search localisation.

From : parsed user question (string).
Using : Geocoding API (external API).
Return : 1 search result, with coordinates (json)
"""

import requests
from grandPyApp.api_config import geocoding

class Geocoding:
    """Search localisation."""

    def __init__(self, parsed_string):
        """Define parameters to create endpoint."""
        search_terms = parsed_string+'.json?' #"bordeaux" # parsed_string # TC
        self.URL = geocoding['URL']+search_terms
        self.PARAMS = {
            "access_token" : geocoding['ACCESS_TOKEN'],
            "country" : geocoding['COUNTRY'],
            "limit": geocoding['RESULTS_LIMIT']
        }
        self.Geocoding_results = self.get_Geocoding()

    def get_Geocoding(self):
        """Create and pass request for Geocoding API (MapBox)."""
        request = requests.get(url=self.URL, params=self.PARAMS)
        return request.json()