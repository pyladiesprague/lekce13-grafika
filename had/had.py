import pyglet
import math
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# ------------------------------------------------------------------ #
# Obrazky snake_frame_1.png a snake_frame_2.png jsou ve slozce lekce13#
# ------------------------------------------------------------------ #

# --- 1. Zakladni okno ----------------------------------------------- #
# pyglet.app.run() spusti smycku udalosti                              #

window = pyglet.window.Window()

# --- 2. Nacteni obrazku a sprite ------------------------------------ #
# Sprite je herni objekt s pozici, rotaci a obrazkem.                 #
# Okno musi existovat driv nez nacteme obrazek — potrebujeme OpenGL.  #

obrazek = pyglet.image.load('../snake_frame_1.png')
had = pyglet.sprite.Sprite(obrazek, x=50, y=50)
had.scale_x = 0.5
had.scale_y = 0.5

# --- 3. Kresleni ---------------------------------------------------- #
# on_draw se zavola pokazde, kdyz Pyglet prekresluje okno.             #
# window.clear() smaze predchozi snemek, jinak by se obrazky           #
# vrstvily pres sebe.                                                  #

def vykresli():
    window.clear()
    had.draw()

window.push_handlers(on_draw=vykresli)

# --- 4. Pohyb — funkce tik ------------------------------------------ #
# schedule_interval vola tik() 30x za sekundu.                        #
# Parametr dt = cas od posledniho zavolani (~0.033 s).               #
# Fyzikalni vzorec: nova pozice = stara pozice + rychlost x cas       #

def tik(dt):
    had.x = had.x + dt * 100   # pohyb doprava rychlosti 100 px/s

pyglet.clock.schedule_interval(tik, 1/30)

# --- 5. Vlneni ------------------------------------------------------- #
# Misto primého pohybu zkusime vlnovy pohyb pomoci sin().              #
# Odkomenuj a zakomenuj predchozi tik().

# def tik(dt):
#     had.x = had.x + dt * 100
#     had.y = 150 + 100 * math.sin(had.x / 30)

# --- 6. Rotace ------------------------------------------------------- #
# had.rotation je uhel ve stupnich, roste po kazdem tiku.             #
# Zkus pridat do funkce tik():
#     had.rotation = had.rotation + 2

# --- 7. Prepinani obrazku ------------------------------------------- #
# schedule_once zavola funkci jednou za dany cas (ne opakovaně).      #
# Retezenim schedule_once vytvorime animaci prepinani snimku.         #

obrazek2 = pyglet.image.load('../snake_frame_2.png')

def zmen(dt):
    had.image = obrazek2
    pyglet.clock.schedule_once(zmen_zpatky, 0.2)

def zmen_zpatky(dt):
    had.image = obrazek
    pyglet.clock.schedule_once(zmen, 0.2)

pyglet.clock.schedule_once(zmen, 0.2)

# --- 8. Mys ---------------------------------------------------------- #
# on_mouse_press dostane souradnice kliknuti a cislo tlacitka.        #
# Premistime hada tam, kam klikneme.                                   #

def klik(x, y, tlacitko, modifikatory):
    had.x = x
    had.y = y

window.push_handlers(on_mouse_press=klik)

# --- Spustit --------------------------------------------------------- #
pyglet.app.run()
print('Hotovo!')
