"""Tests file for parser.py."""

import pytest
import requests

from grandPyApp.parser import Parser

class TestParser:
    """Test for class : Parser."""
    
    def test_Parser(self):
        """Parser.py test."""        
        question_send = "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
        assert Parser(question_send).parsed_string == "connais l'adresse d'openclassrooms"

