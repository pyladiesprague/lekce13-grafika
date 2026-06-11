import pyglet
from constants import *
from hra import Hra

window = pyglet.window.Window(width=SIRKA, height=VYSKA)
hra = Hra(window)

window.push_handlers(
    on_draw=hra.vykresli,
    on_key_press=hra.stisk_klavesy,
    on_key_release=hra.pusteni_klavesy,
)
pyglet.clock.schedule(hra.herni_smycka)
pyglet.app.run()
