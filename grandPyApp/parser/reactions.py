"""Reaction file."""

import json
import random


class Reactions:
    """Check if there is expected word in "reactions" dict to generate phrases
    from GrandPyBot.

    In : reactions (dict)
    Act : compare words in "reactions" list, with expected words, like 'HELLO'
          create a string with messages concatanated.
          messages are from "bot_answers.json"
    Out : bonus_message (list).
    """

    def __init__(self, reactions):
        """Open and load bot_answers.json, and launch functions."""
        with open("grandPyApp/static/ressources/bot_answers.json") as data:
            self.bot_answers = json.load(data)
        self.reactions = reactions
        self.bonus_message = []
        self.courtesy()
        self.hello()
        self.how_are()
        self.time()
        self.random_tchat()

    def courtesy(self):
        """Create message reaction from 'COURTESY' words detected."""
        if self.reactions["COURTESY"] != "True":
            self.bonus_message.append(self.bot_answers["COURTESY"])

    def hello(self):
        """Create message reaction from 'HELLO' words detected."""
        if self.reactions["HELLO"] == "True":
            self.bonus_message.append(self.bot_answers["HELLO"])

    def how_are(self):
        """Create message reaction from 'HOW_ARE' words detected."""
        if self.reactions["HOW_ARE"] == "True":
            self.bonus_message.append(self.bot_answers["HOW_ARE"])

    def time(self):
        """Create message reaction from 'TIME' words detected."""
        if self.reactions["TIME"] == "True":
            self.bonus_message.append(self.bot_answers["TIME"])

    def random_tchat(self):
        """Create a random message reaction."""
        self.bonus_message.append(random.choice(self.bot_answers["TCHAT"]))
