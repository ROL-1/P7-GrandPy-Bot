"""Tests file for grandPyApp/parser.py."""

import pytest
import requests

from grandPyApp.parser import Parser

class TestParser:
    """Test for class : Parser."""    
    
    def test_Parser(self):
        """Parser.py main test."""
        question_send = "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"        
        assert Parser(question_send).parsed_string == "salut connais adresse openclassrooms"
    
    def test_Parser_cleaner(self):
        """Parser.py function cleaner() test."""     
        question_send = "TesT !#$%&'()*+,-./:;<=>?@[\]^_`{|}~ tHIs"
        assert Parser(question_send).words_send == ['test', 'this']

    def test_Parser_openStopwords(self):
        """Parser.py function openStopwords() test."""
        assert type(Parser('Test').stopwords_list) == type([])
    
    def test_Parser_addStopwords(self):
        """Parser.py function addStopwords() test."""
        # TC - NO TEST ?
        # https://pypi.org/project/pytest-variables/        
    
    def test_Parser_removeStopwords(self):
        """Parser.py function removeStopwords() test."""
        question_send = "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"        
        assert Parser(question_send).useful_words == ['salut', 'connais', 'adresse', 'openclassrooms']

    def test_Parser_createParsedString(self):
        """Parser.py function createParsedString test."""
        question_send = "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"        
        assert Parser(question_send).parsed_string == "salut connais adresse openclassrooms"
        


