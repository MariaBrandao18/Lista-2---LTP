#Aluna: Maria Eduarda Rodrigues Brandão    RA: 22402382
#Aluna: Júlia Coelho Rodrigues             RA: 22408388

import turtle

#Classe base Forma:

class Forma:

    def __init__ (self):
        self.t = turtle.Turtle()

    def desenhar (self):
        pass

    def reset (self):
        self.t.reset()

#Subclasse Circulo

class Circulo(Forma):

    def __init__ (self, raio):
        super().__init__()
        self.raio = raio
    
    def desenhar(self):
        self.t.circle(self.raio)

class Quadrado(Forma):
    def __init__ (self, lado):
        super().__init__()
        self.lado = lado
    
    def desenhar(self):
        for i in range (4):
            self.t.forward(self.lado)
            self.t.right(90)

# Testando as classes
if __name__ == "__main__":
    
    # Desenhar um círculo
    circulo = Circulo(100)
    circulo.desenhar()

    # Resetar a tela para desenhar outra forma
    circulo.reset()

    # Desenhar um quadrado
    quadrado = Quadrado(100)
    quadrado.desenhar()

    # Finalizar a janela quando clicar
    turtle.done()
