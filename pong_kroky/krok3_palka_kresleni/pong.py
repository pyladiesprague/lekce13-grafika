import pyglet
from constants import *
from mic import Mic
from palka import Palka

mic = Mic()
palka_leva = Palka(x=0)
palka_prava = Palka(x=SIRKA)

def vykresli():
    window.clear()
    mic.vykresli()
    palka_leva.vykresli()
    palka_prava.vykresli()

window = pyglet.window.Window(width=SIRKA, height=VYSKA)
window.push_handlers(on_draw=vykresli)
pyglet.app.run()
