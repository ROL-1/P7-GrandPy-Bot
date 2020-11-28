"""Reaction file. """

import json


class Reactions:
    """

    In : 
    Act :            
    Out : 
    """

    def __init__(self, reactions):
        """"""
        with open('grandPyApp/static/ressources/bot_answers.json') as json_data:
            self.bot_answers = json.load(json_data)
        self.reactions = reactions
        self.bonus_message = []
        self.courtesy()
        self.hello()
        self.how_are()
        self.time()

    def courtesy(self):
        """"""
        if self.reactions['COURTESY'] != 'True':
            self.bonus_message.append(self.bot_answers['BOT_COURTESY'])

    def hello(self):
        if self.reactions['HELLO'] == 'True':
            self.bonus_message.append(self.bot_answers['BOT_HELLO'])

    def how_are(self):
        if self.reactions['HOW_ARE'] == 'True':
            # if self.reactions['TIME_UNIT'] != 'False':
            #     bonus_message.append(self.bot_answers['BOT_HOW_TIME'].format(self.reactions['TIME_UNIT'])) # To upgrade
            # else:
            self.bonus_message.append(self.bot_answers['BOT_HOW_ARE'])

    def time(self):
        if self.reactions['TIME'] == 'True':
            self.bonus_message.append(self.bot_answers['BOT_TIME'])
    
