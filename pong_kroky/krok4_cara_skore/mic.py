from constants import *
from obdelnik import Obdelnik

class Mic(Obdelnik):
    def __init__(self):
        self.x = SIRKA // 2
        self.y = VYSKA // 2

    def vykresli(self):
        super().vykresli(
            self.x - VELIKOST_MICE // 2,
            self.y - VELIKOST_MICE // 2,
            VELIKOST_MICE,
            VELIKOST_MICE,
        )
