import pyglet
import math
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# ------------------------------------------------------------------ #
# Soubor had.png musí být ve stejné složce jako tento skript.        #
# ------------------------------------------------------------------ #

# --- 1. Základní okno ----------------------------------------------- #
# pyglet.app.run() spustí smyčku událostí — program čeká na události  #
# a reaguje na ně. Bez ní by se okno okamžitě zavřelo.                #

window = pyglet.window.Window()

# --- 2. Načtení obrázku a sprite ------------------------------------ #
# Sprite je herní objekt s pozicí, rotací a obrázkem.                 #
# Okno musí existovat dřív než načteme obrázek — potřebujeme OpenGL. #

obrazek = pyglet.image.load('../snake_frame_1.png')
had = pyglet.sprite.Sprite(obrazek, x=50, y=50)
had.scale_x=0.5
had.scale_y=0.5

# --- 3. Kreslení ---------------------------------------------------- #
# on_draw se zavolá pokaždé, když Pyglet překreslí okno.              #
# window.clear() smaže předchozí snímek, jinak by se obrázky          #
# "vrstvily" přes sebe.                                               #

def vykresli():
    window.clear()
    had.draw()

window.push_handlers(on_draw=vykresli)

# --- 4. Pohyb — funkce tik ------------------------------------------ #
# schedule_interval volá tik() 30× za sekundu.                        #
# Parametr dt = čas od posledního zavolání (≈ 0.033 s).              #
# Fyzikální vzorec: nová pozice = stará pozice + rychlost × čas      #

def tik(dt):
    had.x = had.x + dt * 100   # pohyb doprava rychlostí 100 px/s

pyglet.clock.schedule_interval(tik, 1/30)

# --- 5. Vlnění ------------------------------------------------------- #
# Místo přímého pohybu zkusíme vlnový pohyb pomocí sin().             #
# had.x roste lineárně, had.y se mění jako sinusoida.                 #
# Odkomentuj a zakomentuj předchozí tik(), aby obě najednou nefungovaly.

# def tik(dt):
#     had.x = had.x + dt * 100
#     had.y = 150 + 100 * math.sin(had.x / 30)

# --- 6. Rotace ------------------------------------------------------- #
# had.rotation je úhel ve stupních, roste po každém tiku.             #
# Zkus přidat do funkce tik():
#     had.rotation = had.rotation + 2

# --- 7. Přepínání obrázků ------------------------------------------- #
# schedule_once zavolá funkci jednou za daný čas (ne opakovaně).      #
# Řetězením schedule_once vytvoříme animaci přepínání snímků.         #

obrazek2 = pyglet.image.load('../snake_frame_2.png')

def zmen(dt):
    had.image = obrazek2
    pyglet.clock.schedule_once(zmen_zpatky, 0.2)

def zmen_zpatky(dt):
    had.image = obrazek
    pyglet.clock.schedule_once(zmen, 0.2)

pyglet.clock.schedule_once(zmen, 0.2)

# --- 8. Myš ---------------------------------------------------------- #
# on_mouse_press dostane souřadnice kliknutí a číslo tlačítka.        #
# Přemístíme hada tam, kam klikneme.                                  #

def klik(x, y, tlacitko, modifikatory):
    had.x = x
    had.y = y

window.push_handlers(on_mouse_press=klik)

# --- Spustit --------------------------------------------------------- #
pyglet.app.run()
print('Hotovo!')
