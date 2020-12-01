"""Interprets useful words."""

import json
import re


class Interpreter:
    """Interprets useful words.

    In : parsed_string (string)
    Act :  compares words with several lists of lexical fields,
          to identify different reactions to be generated.
    Out : list of key words for each expected reaction.
    """

    def __init__(self, parsed_string):
        """Load question send by user."""
        self.reactions = {
            "COURTESY": "False",
            "HELLO": "False",
            "HOW_ARE": "False",
            "TIME": "False",  # For next feature
            "TIME_UNIT": "False",  # For next feature
        }
        self.reactlist = []
        self.parsed_string = parsed_string.split()
        self._lexicals()
        self.better_words = self._interpreter()
        self._edit_reactions()

    def _lexicals(self):
        """Open and read "stopwords.json" file.

        create a variable "lexicals" (type 'list').
        """
        with open("grandPyApp/static/ressources/lexicals.json") as json_data:
            self.lexicals = json.load(json_data)

    def _interpreter(self):
        """Inspect parsed_string looking for words starting by expected
        radicals.

        Return a "better_words" list without them.
        """
        trashlist = []
        for word in self.parsed_string:
            dic = self.lexicals
            for k, v in dic.items():
                for radical in v:
                    found = re.match(radical, word)
                    if found:
                        self.reactlist.append(k)
                        trashlist.append(word)
        better_words = \
            " ".join([x for x in self.parsed_string if x not in trashlist])
        return better_words

    def _edit_reactions(self):
        """Edit 'reactions' dict,

        change values "True" if key is in 'reactlist'
        """
        for reaction in self.reactlist:
            if reaction not in ["REJECT", "LOCALISE"]:
                self.reactions[reaction] = "True"
