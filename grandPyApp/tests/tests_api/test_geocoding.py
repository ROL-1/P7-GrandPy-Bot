"""Tests file for grandPyApp/geocoding.py."""

from grandPyApp.api.geocoding import Geocoding


class TestGeocoding:
    """Test for class : Geocoding."""

    def test_geocoding_OK(self, monkeypatch):
        """geocoding.py test with result."""
        parsed_string = "Bordeaux"
        results = {
            "type": "FeatureCollection",
            "query": ["bordeaux"],
            "features": [
                {
                    "id": "place.7230196621811150",
                    "type": "Feature",
                    "place_type": ["place"],
                    "relevance": 1,
                    "properties": {"wikidata": "Q1479"},
                    "text": "Bordeaux",
                    "place_name": "Bordeaux, Gironde, France",
                    "bbox": [-0.638626, 44.81077, -0.533675, 44.915545],
                    "center": [-0.57944, 44.83778],
                    "geometry": {"type": "Point", "coordinates":
                                 [-0.57944, 44.83778]},
                    "context": [
                        {
                            "id": "region.12909948074787080",
                            "wikidata": "Q12526",
                            "short_code": "FR-33",
                            "text": "Gironde",
                        },
                        {
                            "id": "country.19008108158641660",
                            "wikidata": "Q142",
                            "short_code": "fr",
                            "text": "France",
                        },
                    ],
                }
            ],
            "attribution": "NOTICE: © 2020 Mapbox and its suppliers. All rights reserved. \
            Use of this data is subject to the Mapbox Terms of Service \
            (https://www.mapbox.com/about/maps/). \
            This response and the information it contains may not be retained.\
            POI(s) provided by Foursquare.",
        }

        def mock_get_geocoding(self):
            """Mock function for get_geocoding."""
            return results

        monkeypatch.setattr(Geocoding, "get_geocoding", mock_get_geocoding)

        g = Geocoding(parsed_string)
        assert g.response == results
        assert g.coord == results["features"][0]["center"]
        assert g.adress == results["features"][0]["place_name"]

    def test_geocoding_NOK(self, monkeypatch):
        """geocoding.py test without result."""
        parsed_string = "Bordeaux"

        def mock_get_geocoding_NOK(self):
            """Mock function for get_geocoding."""
            return {}

        monkeypatch.setattr(Geocoding, "get_geocoding", mock_get_geocoding_NOK)

        g = Geocoding(parsed_string)
        assert g.response == {}
