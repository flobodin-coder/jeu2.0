import pyxel

solide_tile = [(0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (7, 0), (7, 1), (7, 2), (7, 3), (7, 4)]
"""for i in  range(8):
    for j in range(5):
        if i >= 5 or j >= 4:
            solide_tile.append((i,j))"""


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = 3
        self.vy = 3
        self.is_right = True

    def update(self):
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x -= self.vx
            self.is_right = False
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x += self.vx
            self.is_right = True
        if pyxel.btn(pyxel.KEY_UP):
            self.y -= self.vy
        if pyxel.btn(pyxel.KEY_DOWN):
            self.y += self.vy

    def draw(self):
        #pyxel.rect(self.x, self.y, 8, 8, 9)
        w = 8 if self.is_right else -8
        pyxel.blt(self.x, self.y, 0, 0, 16, w , 8, 2)



class App:
    def __init__(self):
        pyxel.init(128, 128)
        pyxel.load("1.pyxres")
        self.player = Player(50, 50)
        pyxel.run(self.update, self.draw)

    def update(self):
        self.player.update()

    def draw(self):
        pyxel.cls(0)
        pyxel.bltm(0, 0, 0, 0, 0, 128, 128)
        self.player.draw()

App()