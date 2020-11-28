"""Tests file for grandPyApp/wikipedia.py."""

from grandPyApp.api.wikipedia import WikiApi


class TestWikiApi:
    """Test for class : WikiApi."""

    def test_WikiApi(self, monkeypatch):
        """wikipedia.py test."""
        parsed_string = ""
        results = {
            "batchcomplete": "",
            "continue": {"gsroffset": 1, "continue": "gsroffset||"},
            "query": {
                "pages": {
                    "3973632": {
                        "pageid": 3973632,
                        "ns": 0,
                        "title": "Bordeaux",
                        "index": 1,
                        "extract": "Bordeaux (/bɔʁ.do/) ...",
                        "coordinates": [
                            {
                                "lat": 44.837912,
                                "lon": -0.579541,
                                "primary": "",
                                "globe": "earth",
                            }
                        ],
                    }
                }
            },
        }

        def mock_WikiApi(self):
            return results

        monkeypatch.setattr(WikiApi, "wiki_request", mock_WikiApi)

        w = WikiApi(parsed_string)
        assert w.wiki_results == results
