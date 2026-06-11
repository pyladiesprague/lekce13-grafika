import pyglet
from pyglet.window import key
from constants import *
from obdelnik import Obdelnik
from mic import Mic
from palka import Palka

mic = Mic()
palka_leva = Palka(x=0)
palka_prava = Palka(x=SIRKA)
skore = [0, 0]
stisknute_klavesy = set()

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

def stisk_klavesy(symbol, modifikatory):
    if symbol == key.W:
        stisknute_klavesy.add(('nahoru', 0))
    if symbol == key.S:
        stisknute_klavesy.add(('dolu', 0))
    if symbol == key.UP:
        stisknute_klavesy.add(('nahoru', 1))
    if symbol == key.DOWN:
        stisknute_klavesy.add(('dolu', 1))

def pusteni_klavesy(symbol, modifikatory):
    if symbol == key.W:
        stisknute_klavesy.discard(('nahoru', 0))
    if symbol == key.S:
        stisknute_klavesy.discard(('dolu', 0))
    if symbol == key.UP:
        stisknute_klavesy.discard(('nahoru', 1))
    if symbol == key.DOWN:
        stisknute_klavesy.discard(('dolu', 1))

def herni_smycka(dt):
    palka_leva.pohyb(dt,
                     nahoru=('nahoru', 0) in stisknute_klavesy,
                     dolu=('dolu', 0) in stisknute_klavesy)
    palka_prava.pohyb(dt,
                      nahoru=('nahoru', 1) in stisknute_klavesy,
                      dolu=('dolu', 1) in stisknute_klavesy)

window = pyglet.window.Window(width=SIRKA, height=VYSKA)
window.push_handlers(
    on_draw=vykresli,
    on_key_press=stisk_klavesy,
    on_key_release=pusteni_klavesy,
)
pyglet.clock.schedule(herni_smycka)
pyglet.app.run()
