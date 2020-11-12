"""Tests file for grandPyApp/wikipedia.py."""

import pytest
import requests

from grandPyApp.wikipedia import WikiApi

class TestWikiApi:
    """Test for class : WikiApi."""

    def test_WikiApi(self, monkeypatch):
        """wikipedia.py test."""
        parsed_string = "bordeaux"
        results = {'batchcomplete': '', 'continue': {'gsroffset': 1, 'continue': 'gsroffset||'}, 'query': {'pages': {'3973632': {'pageid': 3973632, 'ns': 0, 'title': 'Bordeaux', 'index': 1, 'extract': "Bordeaux (/bɔʁ.do/) est une commune du Sud-Ouest de la France. Capitale de la Gaule aquitaine sous l'Empire romain pendant près de 200 ans ; puis du Duché d'Aquitaine, de la province royale de Guyenne et du siècle des lumières, elle est aujourd'hui le chef-lieu et la préfecture de la région Nouvelle-Aquitaine, du département de la Gironde et le siège de Bordeaux Métropole.\nAu 1er janvier 2017, elle est la neuvième commune de France par sa population avec 254 436 habitants.", 'coordinates': [{'lat': 44.837912, 'lon': -0.579541, 'primary': '', 'globe': 'earth'}]}}}}

        def mock_WikiApi(self):
            return results
        
        monkeypatch.setattr(WikiApi, 'wiki_request', mock_WikiApi)

        w = WikiApi(parsed_string)
        assert w.wiki_results == results