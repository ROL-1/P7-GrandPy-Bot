"""Tests file."""

import pytest
import requests

from grandPyApp.parser import Parser

class Test_Parser:
    """Test for class : Parser."""
    
    def test_Parser(self):
        """Parser.py tests."""        
        question_send = "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
        assert Parser(question_send).parsed_string == "connais l'adresse d'openclassrooms"
