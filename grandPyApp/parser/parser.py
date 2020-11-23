"""Parser file. Remove unuseful words from a string. Return a list of words."""

import json

from grandPyApp.parser.cleaner import Cleaner

class Parser:
    """Parse user question to keep useful words.

    In : user's question_send (string)
    Act :       
        Remove words find in "stopwords.json" or "new_words" list.
    Out : make .parsed_string (string) accessible for main.py.
    """

    def __init__(self, question_send):  
        """Load question send by user."""  
        self.question_send = question_send
        self.stopwords_list = []
        self.useful_words = []
        self.parsed_string = ''
        self.parse()
    
    def parse(self):
        """Launch functions for class : Parser."""
        self.question_cleaned = Cleaner(self.question_send).question_cleaned
        self.openStopwords()
        self.addStopwords()
        self.removeStopwords()
        self.createParsedString()

    def openStopwords(self):
        """Open and read "stopwords.json" file."""
        with open('grandPyApp/static/ressources/stopwords_fr.json') as json_data:
            self.stopwords_list = json.load(json_data)

    def addStopwords(self):
        """Extend stopwords list with personals words."""
        new_words = ['salut','grandpy','py','plait','plaît'] #TC - MOVE TO CONFIG
        self.stopwords_list.extend(new_words)

    def removeStopwords(self):
        """Create "useful_words" list by not selecting words from the reject lists."""        
        for word in self.question_cleaned :
            if word not in self.stopwords_list:
                self.useful_words.append(word)

    def createParsedString(self):
        """Create "parsed _string" with only useful words."""
        self.parsed_string = (' ').join(self.useful_words)
        print('\n###parsed_string### : ', self.parsed_string) #TC
        return self.parsed_string
        
# a = Parser("Salut grandpy! Comment s'est passé ta soirée avec Grandma hier soir? Au fait, pendant que j'y pense, pourrais-tu m'indiquer où se trouve le musée d'art et d'histoire de Fribourg, s'il te plaît?")
