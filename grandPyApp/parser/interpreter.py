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
        self.words = parsed_string.split()
        self.better_words = self._lexical_fields()

    def _lexical_fields(self):
        """Search words starting by."""
        LOCALISE = ["^adres","^indiqu","^situ","^localis","^trouv","^degot","^procur","^donn","^cherch","^obten","^recuper"]
        trashlist = []
        for w in self.words:
            for l in LOCALISE:                
                found = re.match(l,w)
                if found:
                    trashlist.append(w)
        better_words = ' '.join([x for x in self.words if x not in trashlist])
        return better_words

       

# I = Interpreter("indiquer où se trouve le musée d'art et d'histoire de Fribourg")

# "Salut grandpy! Comment s'est passé ta soirée avec Grandma hier soir? Au fait, pendant que j'y pense, pourrais-tu m'indiquer où se trouve le musée d'art et d'histoire de Fribourg, s'il te plaît?".
# "Bonsoir Grandpy, j'espère que tu as passé une belle semaine. Est-ce que tu pourrais m'indiquer l'adresse de la tour eiffel? Merci d'avance et salutations à Mamie."

# champs lexicaux sans applications : juste détection et renvoyer message : revenir pour la v2
# séparer par punctuation terminale ?