"""Search localisation with Mediawiki API.

In: parsed user question (string).
Act : Use MediaWiki API (external API).
Out : 1 search result, with introduction (json)
"""

import requests

from grandPyApp.api_config import wikipedia

class WikiApi:
    """Search a localisation with Mediawiki API."""

    def __init__(self, parsed_string): # parsed_string # TC
        """Define parameters to create endpoint."""          
        search_terms = parsed_string #"pont bordeaux" # parsed_string # TC
        self.URL = wikipedia['URL']
        self.PARAMS = {
            "action": "query",
            "prop":"extracts", # return : infos | coordinates
            "explaintext":"1", # text or html (boolean y/n)
            "exintro": "1", # intro (boolean y/n)
            "format": "json",
            "generator": "search", # search method
            "gsrsearch": search_terms, # terms search
            "exsentences": wikipedia['SENTENCES_LIMIT'], # nb sentences
            "gsrlimit": wikipedia['RESULTS_LIMIT'],  # nb results
        }
        self.wiki_results = self.wiki_request()

    def wiki_request(self):
        """Create and pass request for Wiki Media Api."""
        response = requests.get(url=self.URL, params=self.PARAMS)
        return response.json()

# W = WikiApi("bordeaux") # TC
# print(W.wiki_results) # TC