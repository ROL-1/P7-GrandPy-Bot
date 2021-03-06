"""Cleaner file."""

from string import punctuation

import unidecode


class Cleaner:
    """Clean a string. Return a list.

    In : user's question_send (string)
    Act : Change the sentence in lowercase.
            Remove punctuation.
            Remove accentuation.
    Out : make .question_cleaned (list) accessible for parser.py
    """

    def __init__(self, question_send):
        """Launch function clean."""
        self.question_send = question_send
        self.question_cleaned = self._split()

    @property
    def _uncapitalized(self):
        """Uncapitalize string."""
        uncapitalized = self.question_send.lower()
        return uncapitalized

    @property
    def _no_punctuation(self):
        """Remove puncutation."""
        no_punctuation = "".join(
            [i if i not in punctuation else " " for i in self._uncapitalized]
        )
        return no_punctuation

    @property
    def _no_accentuation(self):
        """Remove accentuation."""
        no_accentuation = unidecode.unidecode(self._no_punctuation)
        return no_accentuation

    def _split(self):
        question_cleaned = self._no_accentuation.split()
        return question_cleaned
