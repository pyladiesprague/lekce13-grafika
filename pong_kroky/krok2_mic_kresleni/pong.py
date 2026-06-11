import pyglet
from constants import *
from mic import Mic

mic = Mic()

def vykresli():
    window.clear()
    mic.vykresli()

window = pyglet.window.Window(width=SIRKA, height=VYSKA)
window.push_handlers(on_draw=vykresli)
pyglet.app.run()
