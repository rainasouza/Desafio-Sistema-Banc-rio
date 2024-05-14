from abc import ABC, abstractmethod
from datetime import datetime

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco

class Conta(ABC):
    def __init__(self, numero, cliente):
        self.numero = numero
        self.cliente = cliente
        self.saldo = 0
        self.historico = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.registrar_transacao("Depósito", valor)

    @abstractmethod
    def sacar(self, valor):
        pass

    def registrar_transacao(self, tipo, valor):
        self.historico.append({
            "tipo": tipo,
            "valor": valor,
            "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        })

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500):
        super().__init__(numero, cliente)
        self.limite = limite

    def sacar(self, valor):
        if 0 < valor <= self.saldo + self.limite:
            self.saldo -= valor
            self.registrar_transacao("Saque", valor)

class PessoaFisica(Cliente):
    def __init__(self, nome, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.cpf = cpf


cliente1 = PessoaFisica("Exemplo", "123.456.789-10", "Rua ABC, 123")
conta1 = ContaCorrente("001", cliente1)
conta1.depositar(1000)
conta1.sacar(500)
print(conta1.saldo)  # Saída esperada: 500
