"""Tests file for grandPyApp/parser/interpreter.py."""

from grandPyApp.parser.interpreter import Interpreter


class TestInterpreter:
    """Test for class : Interpreter."""

    # @classmethod
    def setup_class(self):
        """"""
        self.parsed_string = (
            "bonjour comment grand py donne heure adresse musée orsay plait"
        )

    def test_Interpreter(self):
        """Interpreter.py main test.

        Test _interpreter and _edit_reactions.
        """
        i = Interpreter(self.parsed_string)
        assert i.better_words == "grand musée orsay"
        i = Interpreter("hello")
        assert i.reactions == {
            "COURTESY": "False",
            "HELLO": "True",
            "HOW_ARE": "False",
            "TIME": "False",
            "TIME_UNIT": "False",
        }

    def test_lexicals(self):
        """Interpreter.py function _lexicals test."""
        i = Interpreter(self.parsed_string)
        assert isinstance(i.lexicals, dict)
