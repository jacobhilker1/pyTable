import random
class Coin:
    def __init__(self):
        self.heads = 0
        self.tails = 1
    def flip(self):
        if random.randint(0, 1) % 2 == 0:
            return True
        return False 
