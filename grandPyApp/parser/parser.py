"""Parser file. Remove unuseful words from a string. Return a list of words."""

import json

from string import punctuation

class Parser:
    """Parse user question to keep useful words.

    In : user question (string)
    Act : 
        Change the sentence in lowercase.
        Remove punctuation.
        Remove words find in "stopwords.json" or "new_words" list.
    Out : Return parsed_string (string) with words separates by spaces.
    """

    def __init__(self, question_send):  
        """Load question send by user."""  
        self.question_send = question_send
        self.words_send = []
        self.stopwords_list = []
        self.useful_words = []
        self.parsed_string = ''
        self.parse()
    
    def parse(self):
        """Launch functions."""
        self.cleaner()
        self.openStopwords()
        self.addStopwords()
        self.removeStopwords()
        self.createParsedString()

    def cleaner(self):
        """Remove punctuation and split the string to return a list."""
        lower_string = self.question_send.lower()
        no_punctuation = ''.join([i if i not in punctuation else ' ' for i in lower_string])
        self.words_send = no_punctuation.split()
        
    def openStopwords(self):
        """Open and read "stopwords.json" file."""
        with open('grandPyApp/static/ressources/stopwords_fr.json') as json_data:
            self.stopwords_list = json.load(json_data)

    def addStopwords(self):
        """Extend stopwords list with personals words."""
        new_words = ['grandpy','py'] #TC - MOVE TO CONFIG
        self.stopwords_list.extend(new_words)

    def removeStopwords(self):
        """Create "useful_words" list by not selecting words from the reject lists."""        
        for word in self.words_send :
            if word not in self.stopwords_list:
                self.useful_words.append(word)

    def createParsedString(self):
        """Create "parsed _string" with only useful words."""
        self.parsed_string = (' ').join(self.useful_words)
        print('\n###parsed_string### : ', self.parsed_string) #TC
        return self.parsed_string
        
# a = Parser("Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?")
