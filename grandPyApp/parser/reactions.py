"""Reaction file."""

import json
import random


class Reactions:
    """

    In :
    Act :
    Out :
    """

    def __init__(self, reactions):
        """"""
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
        """"""
        if self.reactions["COURTESY"] != "True":
            self.bonus_message.append(self.bot_answers["BOT_COURTESY"])

    def hello(self):
        if self.reactions["HELLO"] == "True":
            self.bonus_message.append(self.bot_answers["BOT_HELLO"])

    def how_are(self):
        if self.reactions["HOW_ARE"] == "True":
            self.bonus_message.append(self.bot_answers["BOT_HOW_ARE"])

    def time(self):
        if self.reactions["TIME"] == "True":
            self.bonus_message.append(self.bot_answers["BOT_TIME"])

    def random_tchat(self):
        self.bonus_message.append(random.choice(self.bot_answers["BOT_TCHAT"]))
