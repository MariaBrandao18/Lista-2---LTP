#Aluna: Maria Eduarda Rodrigues Brandão    RA: 22402383
#Aluna: Júlia Coelho Rodrigues             RA: 22408388

from abc import ABC, abstractmethod

class ContaBancaria(ABC):
    def __init__(self, conta, titular, saldo=0):
        self.conta = conta
        self.titular = titular
        self.saldo = saldo

    @abstractmethod
    def sacar(self, valor):
        pass

    @abstractmethod
    def depositar(self, valor):
        pass

    @abstractmethod
    def consultar_saldo(self):
        pass

    @abstractmethod
    def infoDaConta(self):
        pass


class ContaCorrente(ContaBancaria):
    def __init__(self, conta, titular, saldo=0, chequeEspecial=0):
        super().__init__(conta, titular, saldo)
        self.chequeEspecial = chequeEspecial

    def infoDaConta(self):
        print('Número da conta:', self.conta)
        print('Nome do titular:', self.titular)
        print('Saldo da conta:', self.saldo)

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo - valor >= -self.chequeEspecial:
            self.saldo -= valor
            return True
        else:
            print("Saldo insuficiente.")
            return False

    def consultar_saldo(self):
        return self.saldo


class ContaPoupanca(ContaBancaria):
    juros = 0.01

    def __init__(self, conta, titular, saldo=0):
        super().__init__(conta, titular, saldo)

    def infoDaConta(self):
        print('Número da conta:', self.conta)
        print('Nome do titular:', self.titular)
        print('Saldo da conta:', self.saldo)

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo - valor < 0:
            print("Saldo insuficiente.")
            return False
        else:
            self.saldo -= valor
            return True

    def consultar_saldo(self):
        return self.saldo + (self.saldo * self.juros)

conta_corrente = ContaCorrente(conta=12345, titular="João Silva", saldo=500, chequeEspecial=1000)
conta_corrente.infoDaConta()
conta_corrente.depositar(300)
print("Depósito de R$ 300,00:")
conta_corrente.infoDaConta()
conta_corrente.sacar(900)
print("Saque de R$ 900,00:")
conta_corrente.infoDaConta()
conta_corrente.sacar(1500)
print("Saque de R$ 1500,00:")
conta_corrente.infoDaConta()

conta_poupanca = ContaPoupanca(conta=54321, titular="Maria Souza", saldo=1000)
conta_poupanca.infoDaConta()
conta_poupanca.depositar(200)
print("Depósito de R$ 200,00 na conta Poupança:")
conta_poupanca.infoDaConta()
conta_poupanca.sacar(50)
print("Saque de R$ 50,00 na conta Poupança:")
conta_poupanca.infoDaConta()
