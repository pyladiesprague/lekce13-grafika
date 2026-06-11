import pyglet

class Obdelnik:
    def vykresli(self, x, y, sirka, vyska):
        pyglet.shapes.Rectangle(x, y, sirka, vyska, color=(255, 255, 255)).draw()
