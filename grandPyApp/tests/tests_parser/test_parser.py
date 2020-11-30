"""Tests file for grandPyApp/parser/parser.py."""

from grandPyApp.parser.parser import Parser


class TestParser:
    """Test for class : Parser."""

    # @classmethod
    def setup_class(self):
        """"""
        self.question_send = (
            "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
        )

    def test_Parser(self):
        """Parser.py main test."""
        assert (
            Parser(self.question_send).parsed_string
            == "salut grandpy connais adresse openclassrooms"
        )

    def test_stopwords(self):
        """Parser.py function _stopwords test."""
        assert isinstance(Parser(self.question_send)._stopwords, list)

    def test_reject(self):
        """Parser.py function _reject test."""
        assert isinstance(Parser(self.question_send)._reject, list)

    def test_unwanted_words(self):
        """Parser.py function _unwanted_words test."""
        assert isinstance(Parser(self.question_send)._unwanted_words, list)

    def test_useful_words(self):
        """Parser.py function _useful_words test."""
        assert Parser(self.question_send)._useful_words == [
            "salut",
            "grandpy",
            "connais",
            "adresse",
            "openclassrooms",
        ]
