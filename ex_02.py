#Aluna: Maria Eduarda Rodrigues Brandão    RA: 22402383
#Aluna: Júlia Coelho Rodrigues             RA: 22408388

# Classe Motor
class Motor:

    def status(self):
        return "Motor: em boas condições."
    
# Classe Pneu
class Pneu:

    def status(self):
        return "Pneus: com pressão adequada."
    
# Classe Veículo, que herda de Motor e Pneu
class Veiculo(Motor, Pneu):

    def status(self):
        # Chamando o metodo status de Motor e Pneu
        status_motor = Motor.status(self)
        status_pneu = Pneu.status(self)
        return f"{status_motor}\n{status_pneu}"
    
# Testando as classes
if __name__ == "__main__":
    
    carro = Veiculo()
    print(carro.status())
