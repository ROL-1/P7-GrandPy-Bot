"""Tests file for grandPyApp/parser/reactions.py."""

from grandPyApp.parser.reactions import Reactions


class TestReactions:
    """Test for class : Reactions."""

    def test_Parser(self):
        """Parser.py main test."""
        reactions = {
            "COURTESY": "False",
            "HELLO": "True",
            "HOW_ARE": "False",
            "TIME": "False",
            "TIME_UNIT": "False",
        }
        r = Reactions(reactions)
        assert isinstance(r.bonus_message, list)
