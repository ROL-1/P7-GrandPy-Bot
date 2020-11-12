"""Tests file."""

import pytest
import requests

from grandPyApp.parser import Parser
from grandPyApp.wikipedia import WikiApi

# Lancer pytest avec la commande -s

class TestX:
    """Tests."""
    
    def test_Parser(self):
        """Parser.py tests."""        
        question_send = "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
        assert Parser(question_send).parsed_string == "connais l'adresse d'openclassrooms"

    def test_WikiApi(self, monkeypatch):
        """wikipedia.py tests."""
        parsed_string = "pont bordeaux"
        results = {'batchcomplete': '', 'continue': {'gsroffset': 1, 'continue': 'gsroffset||'}, 'query': {'pages': {'3067681': {'pageid': 3067681, 'ns': 0, 'title': 'Pont de pierre (Bordeaux)', 'index': 1, 'extract': 'Le pont de pierre est un pont à voûtes en maçonnerie franchissant la Garonne à Bordeaux. Il permet de relier le centre-ville au quartier de La Bastide, sur la rive droite.\nLe pont de pierre, construit sur ordre de Napoléon Ier entre 1810 et 1822, a été conçu par les ingénieurs  Claude Deschamps et Jean-Baptiste Basilide Billaudel.', 'coordinates': [{'lat': 44.838472, 'lon': -0.562778, 'primary': '', 'globe': 'earth'}]}}}}

        def mock_wiki(self):
            return results
        
        monkeypatch.setattr(WikiApi, 'wiki_request', mock_wiki)

        x = WikiApi(parsed_string)
        assert x.wiki_results == results 

    def test_MapBox(self):
        """MapBox tests."""
            
        # In : text
        # Out : json

        pass

    # Used before each test
    def setUp(self):
        pass

    # Used after each test
    def tearDown(self):
        pass
