"""Interprets useful words."""

import json
import re

class Interpreter:
    """Interprets useful words.

    In : parsed_string (string)
    Act : compare les mots avec plusieurs listes de champs lexicaux pour identifier des réactions différentes à générer
    Out : better_parsed_string et réactions : ???
    """

    def __init__(self, parsed_string):  
        """Load question send by user."""
        self.reactions = {
            "COURTESY":"False",
            "HELLO":"False",
            "HOW_ARE":"False",
            "TIME":"False",
            "TIME_UNIT":"False"
        }
        self.reactlist = []
        self.parsed_string = parsed_string.split()
        self._lexicals()
        self.better_words = self._interpreter()
        self._edit_reactions()

    def _lexicals(self):
        """Open and read "stopwords.json" file. Return a list."""
        with open('grandPyApp/static/ressources/lexicals.json') as json_data:
            self.lexicals = json.load(json_data)

    def _interpreter(self):
        """Search words starting by."""        
        trashlist = []        
        for word in self.parsed_string:
            dic = self.lexicals
            for k,v in dic.items():
                for radical in v:             
                    found = re.match(radical,word)
                    if found:
                        self.reactlist.append(k)
                        trashlist.append(word)
        better_words = ' '.join([x for x in self.parsed_string if x not in trashlist])
        return better_words
    
    def _edit_reactions(self):
        print(self.reactlist)
        print("BEFORE self.reactions",self.reactions)
        for reaction in self.reactlist:
            if reaction not in ['REJECT','LOCALISE']:
                # if reaction == 'TIME_UNIT':
                #     self.reactions['TIME_UNIT'] = reaction  # To upgrade
                # else:
                self.reactions[reaction] = 'True'
        print("AFTER self.reactions",self.reactions)






# I = Interpreter("bonjour comment va tu grand py, donne moi heure et adresse du musée d'orsay s'il te plait")

# "Salut grandpy! Comment s'est passé ta soirée avec Grandma hier soir? Au fait, pendant que j'y pense, pourrais-tu m'indiquer où se trouve le musée d'art et d'histoire de Fribourg, s'il te plaît?".
# "Bonsoir Grandpy, j'espère que tu as passé une belle semaine. Est-ce que tu pourrais m'indiquer l'adresse de la tour eiffel? Merci d'avance et salutations à Mamie."

# champs lexicaux sans applications : juste détection et renvoyer message : revenir pour la v2
# séparer par punctuation terminale ?