import pyglet
from constants import *
from obdelnik import Obdelnik
from mic import Mic
from palka import Palka

mic = Mic()
palka_leva = Palka(x=0)
palka_prava = Palka(x=SIRKA)
skore = [0, 0]

def vykresli_mezicaru():
    cara = Obdelnik()
    for y in range(DELKA_PULICI_CARKY // 2, VYSKA, DELKA_PULICI_CARKY * 2):
        cara.vykresli(SIRKA // 2 - 1, y, 2, DELKA_PULICI_CARKY)

def nakresli_text(text, x, y, pozice_x):
    pyglet.text.Label(
        text, font_size=VELIKOST_FONTU,
        x=x, y=y, anchor_x=pozice_x,
    ).draw()

def vykresli():
    window.clear()
    mic.vykresli()
    palka_leva.vykresli()
    palka_prava.vykresli()
    vykresli_mezicaru()
    nakresli_text(str(skore[0]),
                  x=ODSAZENI_TEXTU,
                  y=VYSKA - ODSAZENI_TEXTU - VELIKOST_FONTU,
                  pozice_x='left')
    nakresli_text(str(skore[1]),
                  x=SIRKA - ODSAZENI_TEXTU,
                  y=VYSKA - ODSAZENI_TEXTU - VELIKOST_FONTU,
                  pozice_x='right')

window = pyglet.window.Window(width=SIRKA, height=VYSKA)
window.push_handlers(on_draw=vykresli)
pyglet.app.run()
