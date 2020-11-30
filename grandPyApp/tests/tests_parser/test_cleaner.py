"""Tests file for grandPyApp/parser/cleaner.py."""

from grandPyApp.parser.cleaner import Cleaner


class TestCleaner:
    """Test for class : Cleaner."""

    def test_Cleaner(self):
        """Cleaner.py main test."""
        question_send = "Salut Ô GrandPy, seigneur des adresses ! Ca a été ta soirée ?"
        assert Cleaner(question_send).question_cleaned == [
            "salut",
            "o",
            "grandpy",
            "seigneur",
            "des",
            "adresses",
            "ca",
            "a",
            "ete",
            "ta",
            "soiree",
        ]

    def test_uncapitalized_string(self):
        """Cleaner.py function _uncapitalized_string test."""
        question_send = "TesT tHIs"
        assert Cleaner(question_send)._uncapitalized_string == "test this"

    def test_no_punctuation(self):
        """Cleaner.py function _no_punctuation test."""
        question_send = "TesT !#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ tHIs"
        assert (
            Cleaner(question_send)._no_punctuation
            == "test                                 this"
        )

    def test_no_accentuation(self):
        """Cleaner.py function _no_accentuation test."""
        question_send = "çÇáéíóúýÁÉÍÓÚÝàèìòùÀÈÌÒÙãõñäëïöüÿÄËÏÖÜÃÕÑâêîôûÂÊÎÔÛ,È,É,Ê,Ë,Û,Ù,Ï,Î,À,Â,Ô,è,é,ê,ë,û,ù,ï,î,à,â,ô,Ç,ç,Ã,ã,Õ,õ"
        assert (
            Cleaner(question_send)._no_accentuation
            == "ccaeiouyaeiouyaeiouaeiouaonaeiouyaeiouaonaeiouaeiou e e e e u u i i a a o e e e e u u i i a a o c c a a o o"
        )

    def test_split(self):
        """Cleaner.py function _split test."""
        question_send = "Salut Ô GrandPy !"
        assert Cleaner(question_send).question_cleaned == ["salut", "o", "grandpy"]
