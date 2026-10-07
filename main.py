import pyxel



class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = 3
        self.vy = 3
        self.cote_tourne = True

    def update(self):
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x -= self.vx
            self.cote_tourne = False
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x += self.vx
            self.cote_tourne = True
        if pyxel.btn(pyxel.KEY_UP):
            self.y -= self.vy
        if pyxel.btn(pyxel.KEY_DOWN):
            self.y += self.vy

    def draw(self):
        #pyxel.rect(self.x, self.y, 8, 8, 9)
        if self.cote_tourne == True :
            pyxel.blt(self.x, self.y, 0, 0, 16, 8, 8, 2)
        else : 
            pyxel.blt(self.x, self.y, 0, 0, 16, -8, 8, 2)



class App:
    def __init__(self):
        pyxel.init(160, 120)
        pyxel.load("1.pyxres")
        self.player = Player(50, 50)
        pyxel.run(self.update, self.draw)

    def update(self):
        self.player.update()

    def draw(self):
        pyxel.cls(0)
        self.player.draw()

App()