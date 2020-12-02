"""Tests file for grandPyApp/wikipedia.py."""

from grandPyApp.api.wikipedia import WikiApi


class TestWikiApi:
    """Test for class : WikiApi."""

    def test_WikiApi_OK(self, monkeypatch):
        """wikipedia.py test with result."""
        geo_coord_results = [-0.579541, 44.837912]
        results_coordsearch = {
            "batchcomplete": "",
            "query": {
                "geosearch": [
                    {
                        "pageid": 3973632,
                        "ns": 0,
                        "title": "Bordeaux",
                        "lat": 44.837912,
                        "lon": -0.579541,
                        "dist": 0,
                        "primary": "",
                    }
                ]
            },
        }
        results_pagewiki = {
            "batchcomplete": "",
            "query": {
                "pages": {
                    "3973632": {
                        "pageid": 3973632,
                        "ns": 0,
                        "title": "Bordeaux",
                        "extract": "Bordeaux (/bɔʁ.do/) est une commune du "
                        "Sud-Ouest de la France. Capitale de la Gaule "
                        "aquitaine sous l'Empire romain pendant près de 200"
                        " ans ; puis du Duché d'Aquitaine, de la province "
                        "royale de Guyenne et du siècle des lumières, elle "
                        "est aujourd'hui le chef-lieu et la préfecture de la"
                        " région Nouvelle-Aquitaine, du département de la "
                        "Gironde et le siège de Bordeaux Métropole.",
                    }
                }
            },
        }

        def mock_coordsearch(self):
            return results_coordsearch

        monkeypatch.setattr(WikiApi, "_coordsearch", mock_coordsearch)

        def mock_pagewiki(self):
            return results_pagewiki

        monkeypatch.setattr(WikiApi, "_pagewiki", mock_pagewiki)

        w = WikiApi(geo_coord_results)
        w.pageid
        assert w.page == results_coordsearch["query"]["geosearch"][0]["pageid"]
        page = 3973632
        assert w.extract == \
            results_pagewiki["query"]["pages"][str(page)]["extract"]
