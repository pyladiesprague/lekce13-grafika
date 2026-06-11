import random
from constants import *
from obdelnik import Obdelnik

class Mic(Obdelnik):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.rychlost_x = 0
        self.rychlost_y = 0
        self.reset()

    def reset(self):
        self.x = SIRKA // 2
        self.y = VYSKA // 2
        # náhodný směr: vlevo nebo vpravo
        if random.randint(0, 1):
            self.rychlost_x = RYCHLOST
        else:
            self.rychlost_x = -RYCHLOST
        self.rychlost_y = random.uniform(-1, 1) * RYCHLOST

    def pohyb(self, dt):
        self.x += self.rychlost_x * dt
        self.y += self.rychlost_y * dt

    def vykresli(self):
        super().vykresli(
            self.x - VELIKOST_MICE // 2,
            self.y - VELIKOST_MICE // 2,
            VELIKOST_MICE,
            VELIKOST_MICE,
        )
