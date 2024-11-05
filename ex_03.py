#Aluna: Maria Eduarda Rodrigues Brandão    RA: 22402383
#Aluna: Júlia Coelho Rodrigues             RA: 22408388

import turtle as tl
import time

class Ponto():
    def _init_(self, x, y):
        self.x = x
        self.y = y
    def goto_ponto(self):
        time.sleep(3)
        tl.penup()
        tl.goto(self.x, self.y)

p1 = Ponto(90,40)
Ponto.goto_ponto(p1)

p2 = Ponto(-25, -75)
Ponto.goto_ponto(p2)

tl.done()
