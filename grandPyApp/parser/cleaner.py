"""Cleaner file. """

import unidecode

from string import punctuation

class Cleaner:
    """Clean a string. Return a list.

    In : user's question_send (string)
    Act : Change the sentence in lowercase.
            Remove punctuation.
            Remove accentuation.
    Out : make .question_cleaned (list) accessible for parser.py
    """

    def __init__(self, question_send):
        """"""
        self.question_send = question_send
        self.question_cleaned = []
        self.lower_string()
        self.no_punctuation()
        self.unicode_normalizer()


    def lower_string(self):
        """"""
        self.lower_string = self.question_send.lower()

    def no_punctuation(self):
        """"""
        self.no_punctuation = ''.join([i if i not in punctuation else ' ' for i in self.lower_string])

    def unicode_normalizer(self):
        """Remove accentuation."""
        no_accentuation = unidecode.unidecode(self.no_punctuation)
        self.question_cleaned = no_accentuation.split()
    