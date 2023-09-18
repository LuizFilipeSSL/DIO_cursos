# Modulo para definição e immplementação das Classes utilizadas
# no programa

class Cliente:
    def __init__(self, *, cpf, nome, tel):
        self.cpf = cpf
        self.nome = nome
        self.tel = tel
    
    def exibir_dados(self):
        print(self.nome)
        print(self.cpf)
        print(self.tel)


class Conta:
    def __init__(self, num_conta, cliente):
        self.ag = '0001'
        self.num_conta = num_conta
        self.cliente = cliente
        self.saldo = 0.00
        self.extrato = []
        self.saque_dia = 0

    def inserir_item_extrato(self, transacao):
        self.extrato.append(transacao)

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        
    

