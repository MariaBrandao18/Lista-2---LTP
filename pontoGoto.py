import turtle as tl

class Ponto():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def goto_ponto(self):
        tl.penup()
        tl.goto(self.x, self.y)

p1 = Ponto(90,40)
Ponto.goto_ponto(p1)

tl.done()
