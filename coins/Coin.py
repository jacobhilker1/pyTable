import random
class Coin:
    def __init__(self):
        self.heads = "heads"
        self.tails = "tails"
    def flip(self):
        if (random.randint(0, 1) % 2 == 0):
            return "heads"
        return "tails"
