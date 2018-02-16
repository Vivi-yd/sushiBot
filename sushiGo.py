#!/usr/bin/env python3

# 108 cards in a standard deck


class Game:
    def __init__(self, player, rounds):
        self.players = players
        self.rounds = rounds
    
    deck = {
        'tempura': 14,
        'dumpling': 14,
        'maki3': 8,
        'maki2': 12,
        'maki1': 6,
        'sal_nigiri': 10,
        'squ_nigiri': 5,
        'egg_nigiri': 5,
        'pudding': 10,
        'wasabi': 6,
        'chopsticks': 4
    }


    # TODO
    # deal hands to players
    # 10 each in 2-player
    # 9 each in 3-player
    # 8 each in 4-player
    # 7 each in 5-player



class Card:

    def __init__(self, name, card_num):
        self.name = name
        self.card_num = card_num

    # number of cards this type have
    def get_card_number(self):
        return self.card_num






