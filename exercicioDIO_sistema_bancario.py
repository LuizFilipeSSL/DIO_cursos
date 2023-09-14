
# Exercício Curso Python Developer Plataforma DIO.me, Capítulo 1
# SISTEMA BANCARIO PYTHON

menu = """
*****************
[1] - DEPOSITO
[2] - SAQUE
[3] - EXTRATO
[4] - SAIR\n
*****************
>>Digite a opção desejada:
"""
saldo = 0.00
total_saques = 0
items_extrato = []
LIMITE_SAQUES = 3
LIMITE_VALOR = 500.00

while True:
    op = input(menu)
    
    if(op == '1'):
        valor_dep = float(input("\nDigite o valor do depósito: "))
        if valor_dep > 0 :
            saldo += float(valor_dep)
            print("Depósito de R$ {0:.2f} realizado com sucesso. Saldo atual: R$ {1:.2f}".format(valor_dep, saldo))
            items_extrato.append("Depósito...........R$ {0:.2f} C".format(valor_dep))
        else:
            print("Digite um valor válido.")
            
    elif (op == '2'):
        if total_saques >= 3:
            print("Desculpe, mas você excedeu o limite diário de 3 saques.")
        else:
            vl_saque = float(input("Informe o valor do saque desejado: "))
            vl_saque = round(vl_saque, 2)
            if vl_saque < 0 or vl_saque > 500:
                print("Digite um valor válido. O valor máximo permitido é R$ 500,00")
            elif vl_saque > saldo:
                print("Saldo indisponível. Seu saldo atual é {:.2f}".format(saldo))
            else:
                saldo -= vl_saque
                print("Saque de R$ {0:.2f} realizado com sucesso. Saldo atual: R$ {1:.2f}".format(vl_saque, saldo))
                items_extrato.append("Saque..............R$ {0:.2f} D".format(vl_saque))
                total_saques += 1
    elif (op == '3'):
        print("********EXTRATO**********")
        for i in items_extrato:
            print('{}'.format(i))
        print("\nSaldo atual........R$ {:.2f}".format(saldo))
    elif (op == '4'):
        break
    else:
        print("Você digitou uma opção inválida. ")
