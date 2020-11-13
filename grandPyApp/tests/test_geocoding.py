"""Tests file for grandPyApp/geocoding.py."""

import pytest
import requests

from grandPyApp.geocoding import Geocoding

class TestGeocoding:
    """Test for class : Geocoding."""

    def test_geocoding(self, monkeypatch):
        """geocoding.py test."""
        parsed_string = "bordeaux"
        results = {'type': 'FeatureCollection', 'query': ['bordeaux'], 'features': [{'id': 'place.7230196621811150', 'type': 'Feature', 'place_type': ['place'], 'relevance': 1, 'properties': {'wikidata': 'Q1479'}, 'text': 'Bordeaux', 'place_name': 'Bordeaux, Gironde, France', 'bbox': [-0.638626, 44.81077, -0.533675, 44.915545], 'center': 
[-0.57944, 44.83778], 'geometry': {'type': 'Point', 'coordinates': [-0.57944, 44.83778]}, 'context': [{'id': 'region.12909948074787080', 'wikidata': 'Q12526', 'short_code': 'FR-33', 'text': 'Gironde'}, {'id': 'country.19008108158641660', 'wikidata': 'Q142', 'short_code': 'fr', 'text': 'France'}]}], 'attribution': 'NOTICE: © 2020 Mapbox and its suppliers. All rights reserved. Use of this data is subject to the Mapbox Terms of Service (https://www.mapbox.com/about/maps/). This response and the information it contains may not be retained. POI(s) provided by Foursquare.'}

        def mock_geocoding(self):
            return results
        
        monkeypatch.setattr(Geocoding, 'get_Geocoding', mock_geocoding)

        G = Geocoding(parsed_string)
        assert G.geocoding_results == results