"""Tests file for grandPyApp/parser.py."""

import requests

from grandPyApp.parser.parser import Parser

class TestParser:
    """Test for class : Parser."""

    # @classmethod
    def setup_class(self):
        """"""
        self.question_send = "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"        
    
    def test_Parser(self):
        """Parser.py main test."""      
        assert Parser(self.question_send).parsed_string == "salut connais adresse openclassrooms"
    
    def test_Parser_cleaner(self):
        """Parser.py function cleaner() test."""     
        question_send = "TesT !#$%&'()*+,-./:;<=>?@[\]^_`{|}~ tHIs"
        assert Parser(question_send).words_send == ['test', 'this']

    def test_Parser_removeStopwords(self):
        """Parser.py function removeStopwords() test."""   
        assert Parser(self.question_send).useful_words == ['salut', 'connais', 'adresse', 'openclassrooms']

    def test_Parser_createParsedString(self):
        """Parser.py function createParsedString test."""    
        assert Parser(self.question_send).parsed_string == "salut connais adresse openclassrooms"
        


