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
        assert Parser(question_send).parsed_string == "grandpy connais l'adresse d'openclassrooms"
       
        # IN : une question type
        # Salut grandpy! Comment s'est passé ta soirée avec Grandma hier soir? Au fait, pendant que j'y pense, pourrais-tu m'indiquer où se trouve le musée d'art et d'histoire de Fribourg, s'il te plaît?"
        # Bonsoir Grandpy, j'espère que tu as passé une belle semaine. Est-ce que tu pourrais m'indiquer l'adresse de la tour eiffel? Merci d'avance et salutations à Mamie.
        # Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?
        # OUT : string de mots clefs

    def test_WikiApi(self, monkeypatch):
        """wikipedia.py tests."""
        results =
        fake_result =  

        def mock_wiki():
            return fake_result
        
        monkeypatch.setattr(f, 'a', mock_wiki)

        X = f()
        assert X.a == results        
        


    def test_MapBox(self):
        pass
        

    # Used before each test
    def setUp(self):
        pass

    # Used after each test
    def tearDown(self):
        pass
