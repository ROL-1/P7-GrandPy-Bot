"""Parser file. Remove unuseful words from a string. Return a list of words."""

import json

from string import punctuation

class Parser:
    """Parse user question to keep useful words."""

    def __init__(self, question_send):  
        """Load question send by user."""  
        self.question_send = question_send
        self.words_send = []
        self.parsed_string = ''
        self.cleaner()
        self.parseWords()

    def cleaner(self):
        """Split the string from user question, and remove punctuation."""
        lower_string = self.question_send.lower()
        no_punctuation_list = [i.strip(punctuation) for i in lower_string.split()]         
        for word in no_punctuation_list:
            if word != '':
                self.words_send.append(word)
        # print('words_send', self.words_send) #TC

    def parseWords(self):
        """Create "useful_words" list by not selecting words from the reject lists."""
        with open('grandPyApp/stopwords_fr.json') as json_data:
            stopwords_list = json.load(json_data)
        
        # Add specifics words to the rejected list :
        new_words = ['est-ce','salut','grandpy','py'] #TC - CONFIG
        stopwords_list.extend(new_words)

        # Remove empty words
        useful_words = []
        for word in self.words_send :
            if word not in stopwords_list:
                useful_words.append(word)

        # Change list in string
        self.parsed_string = (' ').join(useful_words)

        # print('self.parsed_string', self.parsed_string) #TC
        return self.parsed_string
        
# a = Parser("Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?")
# print(a.parsed_string)

# Parser

# Récupérer la string
# Découper la string en mots
## créer liste de mots (séparés par espace)
# Retirer les mots inutiles
## "liste mots retenus" = []
## if "mot" in NOTIN "liste_stopwords" => add "mot" in "liste mots retenus"
# Retirer caractères spéciaux
# Retourner "liste de mots retenus" 