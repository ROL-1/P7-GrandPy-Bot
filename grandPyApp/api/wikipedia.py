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
        self.URL = wikipedia["URL"]
        self.geo_coord_results = geo_coord_results

    def _coordsearch(self):
        """Create request for Wiki Media Api to search pageid."""
        long = self.geo_coord_results[0]
        lat = self.geo_coord_results[1]
        params = {
            "action": "query",
            "list": "geosearch",
            "gscoord": f"{lat}|{long}",
            "gsradius": 10000,
            "gslimit": 1,
            "format": "json",
        }
        print("response called !!!!!!!!!!!!!!!!!!!")
        response = requests.get(url=self.URL, params=params)
        if response.status_code == 200:
            self.coord_err = False
        else:
            self.coord_err = True
        return response.json()

    @property
    def pageid(self):
        """Return wikipedia page id for second search."""
        page = self._coordsearch()
        self.page = page["query"]["geosearch"][0]["pageid"]

    def _pagewiki(self):
        """Create request for Wiki Media Api to open pageid."""
        params = {
            "pageids": self.page,
            "action": "query",
            "prop": "extracts",
            "explaintext": "1",
            "exintro": "1",
            "format": "json",
            "exsentences": wikipedia["SENTENCES_LIMIT"],
        }

        response = requests.get(url=self.URL, params=params)
        if response.status_code == 200:
            self.pagewiki_err = False
        else:
            self.pagewiki_err = True
        return response.json()

    @property
    def extract(self):
        """Return informations for grandpy story."""
        infos = self._pagewiki()
        return infos["query"]["pages"][str(self.page)]["extract"]
