
# Exercício Curso Python Developer Plataforma DIO.me, Capítulo 1
# SISTEMA BANCARIO PYTHON
# Versão 3 com implementação utilizando classes e integrando-as às 
# funcionalidades do programa 

from classes import *

menu = """
==============================================
[1] - DEPOSITO
[2] - SAQUE
[3] - EXTRATO
[4] - CADASTRAR CLIENTE
[5] - ABRIR CONTA
[6] - LISTA CLIENTES
[7] - LISTA CONTAS
[8] - SAIR
==============================================
>>Digite a opção desejada:
"""
clientes = {}
contas = {}
num_conta = 0
LIMITE_VALOR = 500.00

def exibir_mensagem(msg):
    print("\n==============================================")
    print(msg)
    print("==============================================")
    
def cadastrar_cliente(*, cpf, nome, tel):
    if cpf in clientes:
        exibir_mensagem("Esse cliente já esta cadastrado.")
    else:  
        cli = Cliente(cpf=cpf, nome=nome, tel=tel)
        clientes.update( {cli.cpf: cli} )
        exibir_mensagem("Cliente cadastrado com sucesso.")

def get_cliente(cpf):
    if cpf in clientes:
        return True
    else:
        return False

def abrir_conta(*, cpf):
    if get_cliente(cpf):
        global num_conta
        num_conta += 1
        c = Conta(num_conta, cpf)
        contas.update( {str(c.num_conta): c })
        exibir_mensagem("Conta aberta com sucesso!")
    else:
        exibir_mensagem("Esse cliente não está cadastrado. Efetue o cadastro do cliente primeiro.")

def depositar(*, conta, valor):
    if (conta in contas):
        dep = str("Depósito...........R$ {0:.2f} C".format(valor))
        c = contas[conta]
        c.depositar(valor)
        c.inserir_item_extrato(dep)
        contas[conta] = c
        exibir_mensagem("Deposito realizado com sucesso.")
    else:
        exibir_mensagem('Conta inexistente!')

def validar_conta_saque(*, conta, valor):
    if conta in contas:
        c = contas[conta]
        if c.saque_dia == 3:
            exibir_mensagem("Você excedeu a quantidade diária de saques.")
            return False
        elif c.saldo < valor:
            exibir_mensagem(str("""Você não possui saldo suficiente, seu saldo atual é: """,
                                c.saldo))
            return False
        else:
            return True
    else:
        exibir_mensagem("Conta inexistente.")
        return False
    
def sacar(*, conta, valor):
    saq = "Saque..............R$ {0:.2f} D".format(valor)
    c = contas[conta]
    c.sacar(valor)
    c.extrato.append(saq)
    c.saque_dia += 1
    contas[conta] = c
    exibir_mensagem("Saque realizado com sucesso.")

def acessar_extrato(*, conta):
    if conta in contas:
        c = contas[conta]
        cli = clientes[c.cliente]
        #extrato = contas[conta]['mov']
        print("\n======================EXTRATO========================")
        print("Cliente: ", cli.nome)
        print("Agência: {0}    Conta: {1}\n".format(c.ag, c.num_conta) )
        for i in c.extrato:
            print(i)
        print("\nSaldo atual........R$ {:.2f}".format(c.saldo))
    else:
        exibir_mensagem("Conta inexistente!")

def listar_contas():
    for i in contas:
        c = contas[i]
        msg = str("Agência: {0}    Conta: {1}".format(c.ag, c.num_conta))
        exibir_mensagem(msg)

def listar_clientes():
    for i in clientes:
        cli = clientes[i]
        msg = str("Nome: {0} \nCPF: {1}\nTelefone: {2}".format(cli.nome, cli.cpf, cli.tel))
        exibir_mensagem(msg)

while True:
    op = input(menu)
    
    if(op == '1'):
        vl_dep = float(input("Digite o valor do depósito: "))
        if vl_dep > 0 :
            depositar(conta=input('Digite o número da conta: '), valor=vl_dep)
        else:
            exibir_mensagem("Digite um valor válido.")
            
    elif (op == '2'):
        vl_saque = float(input("Informe o valor do saque desejado: "))
        if vl_saque > 0 and vl_saque <= LIMITE_VALOR:
            c = input("Informe a conta para saque: ")
            if validar_conta_saque(conta=c, valor=vl_saque):
                sacar(conta=c, valor=vl_saque)
        else:
            exibir_mensagem("Digite um valor válido.")
        
    elif (op == '3'):
        acessar_extrato(conta=input("Digite o número da conta: "))

    elif(op == '4'):
        cadastrar_cliente(cpf = input("Digite o cpf do cliente: "),
                         nome = input("Digite o nome do cliente: ").upper(),
                         tel=input("Digite o telefone do cliente: "))
        
    elif (op=='5'):
        abrir_conta(cpf=input("Digite o cpf do cliente: "))

    elif(op=='6'):
        listar_clientes()

    elif(op=='7'):
        listar_contas()

    elif (op=='8'):
        break

    else:
        exibir_mensagem("Você digitou uma opção inválida. ")
