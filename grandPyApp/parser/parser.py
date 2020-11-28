"""Parser file.

Remove unuseful words from a string. Return a list of words.
"""

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
        self.question_cleaned = Cleaner(question_send).question_cleaned
        self.parsed_string = self._parse()

    @property
    def _stopwords(self):
        """Open and read "stopwords.json" file.

        Return a list.
        """
        with open("grandPyApp/static/ressources/stopwords_fr.json") as data:
            stopwords_list = json.load(data)
        return stopwords_list

    @property
    def _reject(self):
        """Open and read "stopwords.json" file.

        Return a list.
        """
        with open("grandPyApp/static/ressources/lexicals.json") as data:
            _reject = json.load(data)["REJECT"]
        return _reject

    @property
    def _unwanted_words(self):
        """Extend stopwords_list with personals words.

        Return a list.
        """
        unwanted_words_list = self._stopwords + self._reject
        return unwanted_words_list

    @property
    def _useful_words(self):
        """Create"useful words list by not selecting words from the reject
        list."""
        useful_words_list = []
        for word in self.question_cleaned:
            if word not in self._unwanted_words:
                useful_words_list.append(word)
        return useful_words_list

    def _parse(self):
        """Create "parsed _string" with only useful words."""
        parsed_string = (" ").join(self._useful_words)
        return parsed_string


# a = Parser("Salut grandpy! Comment s'est passé ta soirée avec Grandma hier soir? Au fait, pendant que j'y pense, pourrais-tu m'indiquer où se trouve le musée d'art et d'histoire de Fribourg, s'il te plaît?")
