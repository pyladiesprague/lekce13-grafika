import pyglet
from pyglet.window import key
from constants import *
from obdelnik import Obdelnik
from mic import Mic
from palka import Palka

class Hra:
    def __init__(self, window):
        self.window = window
        self.mic = Mic()
        self.palka_leva = Palka(x=0)
        self.palka_prava = Palka(x=SIRKA)
        self.stisknute_klavesy = set()
        self.skore = [0, 0]

    def vykresli(self):
        self.window.clear()
        self.mic.vykresli()
        self.palka_leva.vykresli()
        self.palka_prava.vykresli()
        self.vykresli_mezicaru()
        self.nakresli_text(str(self.skore[0]),
                           x=ODSAZENI_TEXTU,
                           y=VYSKA - ODSAZENI_TEXTU - VELIKOST_FONTU,
                           pozice_x='left')
        self.nakresli_text(str(self.skore[1]),
                           x=SIRKA - ODSAZENI_TEXTU,
                           y=VYSKA - ODSAZENI_TEXTU - VELIKOST_FONTU,
                           pozice_x='right')

    def vykresli_mezicaru(self):
        cara = Obdelnik()
        for y in range(DELKA_PULICI_CARKY // 2, VYSKA, DELKA_PULICI_CARKY * 2):
            cara.vykresli(SIRKA // 2 - 1, y, 2, DELKA_PULICI_CARKY)

    def nakresli_text(self, text, x, y, pozice_x):
        pyglet.text.Label(
            text, font_size=VELIKOST_FONTU,
            x=x, y=y, anchor_x=pozice_x,
        ).draw()

    def zkontroluj_odrazy(self):
        if self.mic.y < VELIKOST_MICE // 2:
            self.mic.rychlost_y = abs(self.mic.rychlost_y)
        if self.mic.y > VYSKA - VELIKOST_MICE // 2:
            self.mic.rychlost_y = -abs(self.mic.rychlost_y)

        palka_min = self.mic.y - VELIKOST_MICE / 2 - DELKA_PALKY / 2
        palka_max = self.mic.y + VELIKOST_MICE / 2 + DELKA_PALKY / 2

        if self.mic.x < TLOUSTKA_PALKY + VELIKOST_MICE / 2:
            if palka_min < self.palka_leva.y < palka_max:
                self.mic.rychlost_x = abs(self.mic.rychlost_x)
            else:
                self.skore[1] += 1
                self.mic.reset()

        if self.mic.x > SIRKA - (TLOUSTKA_PALKY + VELIKOST_MICE / 2):
            if palka_min < self.palka_prava.y < palka_max:
                self.mic.rychlost_x = -abs(self.mic.rychlost_x)
            else:
                self.skore[0] += 1
                self.mic.reset()

    def stisk_klavesy(self, symbol, modifikatory):
        if symbol == key.W:
            self.stisknute_klavesy.add(('nahoru', 0))
        if symbol == key.S:
            self.stisknute_klavesy.add(('dolu', 0))
        if symbol == key.UP:
            self.stisknute_klavesy.add(('nahoru', 1))
        if symbol == key.DOWN:
            self.stisknute_klavesy.add(('dolu', 1))

    def pusteni_klavesy(self, symbol, modifikatory):
        if symbol == key.W:
            self.stisknute_klavesy.discard(('nahoru', 0))
        if symbol == key.S:
            self.stisknute_klavesy.discard(('dolu', 0))
        if symbol == key.UP:
            self.stisknute_klavesy.discard(('nahoru', 1))
        if symbol == key.DOWN:
            self.stisknute_klavesy.discard(('dolu', 1))

    def herni_smycka(self, dt):
        self.palka_leva.pohyb(dt,
                              nahoru=('nahoru', 0) in self.stisknute_klavesy,
                              dolu=('dolu', 0) in self.stisknute_klavesy)
        self.palka_prava.pohyb(dt,
                               nahoru=('nahoru', 1) in self.stisknute_klavesy,
                               dolu=('dolu', 1) in self.stisknute_klavesy)
        self.mic.pohyb(dt)
        self.zkontroluj_odrazy()
