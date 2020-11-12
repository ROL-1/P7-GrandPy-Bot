"""Get wikipedia API informations."""

import requests

class WikiApi:
    """Search a localisation.

    From : a string.
    Return : coordinates ; 3 sentences about the localisation.
    """

    def __init__(self, parsed_string): # parsed_string # TC
        """Init WikiApi."""            
        search_terms = parsed_string #"pont bordeaux" # parsed_string # TC
        self.URL = "https://fr.wikipedia.org/w/api.php"
        self.PARAMS = {
            "action": "query",
            "prop":"extracts|coordinates", # return : infos | coordinates
            "explaintext":"1", # text or html (boolean y/n)
            "exintro": "1", # intro (boolean y/n)
            "format": "json",
            "generator": "search", # how to search
            "gsrsearch": search_terms, # terms search
            "exsentences": "3", # nb sentences
            "gsrlimit":"1",  # nb results
        }
        self.wiki_results = self.wiki_request()

    def wiki_request(self):
        """Create and pass request for Wiki Media Api."""
        request = requests.get(url=self.URL, params=self.PARAMS)
        return request.json()




# W = WikiApi("pont bordeaux") # TC
# print(W.wiki_results) # TC