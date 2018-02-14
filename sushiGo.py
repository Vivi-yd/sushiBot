#!/usr/bin/env python3

# 108 cards in a standard deck
# 14x Tempura
# 14x Dumpling
# 12x 2 Maki rolls
# 8x  3 Maki rolls
# 6 x 1 Maki rolls
# 10x Salmon Nigiri
# 5x  Squid Nigiri
# 5x  Egg Nigiri
# 10x Pudding
# 6x  Wasabi
# 4x  Chopsticks


class Game:
    def __init__(self, player, rounds):
        self.players = players
        self.rounds = rounds

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






