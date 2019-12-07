import random
class Die():
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return random.randint(1,self.sides)

    def roll_times(self,num_rolls):
        for num in range(num_rolls):
            print(self.roll())
