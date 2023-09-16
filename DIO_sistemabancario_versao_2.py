
# Exercício Curso Python Developer Plataforma DIO.me, Capítulo 2
# SISTEMA BANCARIO PYTHON
# Versão aprimorada usando usando as ações através de funções e tratamento
# de cadastro de clientes e contas para vinculação aos depósitos, saques e extratos

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
        clientes.update( {cpf: {"nome": nome, "tel": tel}} )
        exibir_mensagem("Cliente cadastrado com sucesso.")

def get_cliente(cpf):
    if cpf in clientes:
        return dict(clientes.get(cpf, {}))
    else:
        return False

def abrir_conta(*, cpf):
    cli = get_cliente(cpf)
    if cli:
        global num_conta
        conta_nova = num_conta + 1
        num_conta += 1
        contas.update( {
            str(conta_nova): {'ag': '0001', 'cliente': cpf, 'saldo': 0.00, 'mov': [], 'saque_dia':0}
        })
        exibir_mensagem("Conta aberta com sucesso!")
    else:
        exibir_mensagem("Esse cliente não está cadastrado. Efetue o cadastro do cliente primeiro.")

def depositar(*, conta, valor):
    if (conta in contas):
        dep = "Depósito...........R$ {0:.2f} C".format(valor)
        contas[conta]['saldo'] += valor
        contas[conta]['mov'].append(dep)
        exibir_mensagem("Deposito realizado com sucesso.")
    else:
        exibir_mensagem('Conta inexistente!')

def validar_conta_saque(*, conta, valor):
    if conta in contas:
        if contas[conta]['saque_dia'] == 3:
            exibir_mensagem("Você excedeu a quantidade diária de saques.")
            return False
        elif contas[conta]['saldo'] < valor:
            exibir_mensagem(str("""Você não possui saldo suficiente, seu saldo atual é: """,contas[conta]['saldo']))
            return False
        else:
            return True
    else:
        exibir_mensagem("Conta inexistente.")
        return False
    
def sacar(*, conta, valor):
    saq = "Saque..............R$ {0:.2f} D".format(valor)
    contas[conta]['saldo'] -= valor
    contas[conta]['mov'].append(saq)
    contas[conta]['saque_dia'] += 1
    exibir_mensagem("Saque realizado com sucesso.")

def acessar_extrato(*, conta):
    if conta in contas:
        extrato = contas[conta]['mov']
        print("\n======================EXTRATO========================")
        print("Cliente: ", clientes[contas[conta]['cliente']]['nome'])
        print("Agência: {0}    Conta: {1}\n".format(contas[conta]['ag'], conta) )
        for i in extrato:
            print(i)
        print("\nSaldo atual..........R$ {}".format(contas[conta]['saldo']))
    else:
        exibir_mensagem("Conta inexistente!")

def listar_contas():
    for i in contas:
        msg = str("Agência: {0}    Conta: {1}".format(contas[i]['ag'], i))
        exibir_mensagem(msg)


def listar_clientes():
    for i in clientes:
        msg = str("Nome: {0} \nCPF: {1}\nTelefone: {2}".format(clientes[i]['nome'], i, clientes[i]['tel']))
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
