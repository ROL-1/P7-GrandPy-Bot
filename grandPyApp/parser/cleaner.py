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
        """Laucnh functions."""
        self.question_send = question_send
        self.question_cleaned = self._clean()

    @property
    def _uncapitalized_string(self):
        """Uncapitalize string."""
        uncapitalized_string = self.question_send.lower()
        return uncapitalized_string

    @property
    def _no_punctuation(self):
        """Remove puncutation."""
        no_punctuation = ''.join([i if i not in punctuation else ' ' for i in self._uncapitalized_string])
        return no_punctuation

    @property
    def _no_accentuation(self):
        """Remove accentuation."""
        no_accentuation = unidecode.unidecode(self._no_punctuation)
        return no_accentuation
    
    def _clean(self):
        question_cleaned = self._no_accentuation.split()
        return question_cleaned
