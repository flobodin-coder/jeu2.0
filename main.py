import pyxel



class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = 1
        self.vy = 1

    def update(self):
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x -= self.vx
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x += self.vx
        if pyxel.btn(pyxel.KEY_UP):
            self.y -= self.vy
        if pyxel.btn(pyxel.KEY_DOWN):
            self.y += self.vy

    def draw(self):
        pyxel.rect(self.x, self.y, 8, 8, 9)





class App:
    def __init__(self):
        pyxel.init(160, 120)
        self.player = Player(50, 50)
        pyxel.run(self.update, self.draw)

    def update(self):
        self.player.update()

    def draw(self):
        pyxel.cls(0)
        self.player.draw()

App()