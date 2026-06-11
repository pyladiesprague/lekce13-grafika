from lekce13.pong.constants import *
from lekce13.pong.obdelnik import Obdelnik

class Palka(Obdelnik):
    def __init__(self, x):
        self.x = x
        self.y = VYSKA // 2

    def pohyb(self, dt, nahoru, dolu):
        if nahoru:
            self.y += RYCHLOST_PALKY * dt
        if dolu:
            self.y -= RYCHLOST_PALKY * dt
        if self.y < DELKA_PALKY / 2:
            self.y = DELKA_PALKY / 2
        if self.y > VYSKA - DELKA_PALKY / 2:
            self.y = VYSKA - DELKA_PALKY / 2

    def vykresli(self):
        super().vykresli(
            self.x - TLOUSTKA_PALKY,
            self.y - DELKA_PALKY // 2,
            TLOUSTKA_PALKY * 2,
            DELKA_PALKY,
        )
