from constants import *
from obdelnik import Obdelnik

class Palka(Obdelnik):
    def __init__(self, x):
        self.x = x
        self.y = VYSKA // 2

    def vykresli(self):
        super().vykresli(
            self.x - TLOUSTKA_PALKY,
            self.y - DELKA_PALKY // 2,
            TLOUSTKA_PALKY * 2,
            DELKA_PALKY,
        )
