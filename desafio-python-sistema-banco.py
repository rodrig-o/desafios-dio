# criar um sistema bancário para controlar depósitos e saques
# permitir depositar apenas valores positivos
# gerar um relatório com o total de depósitos realizados
# permitir 3 saques diários de até R$ 500,00 cada
# gerar um relatório com o total de saques realizados

import datetime
from datetime import date, timedelta

LIMITE_SAQUE = 3
LIMITE_SAQUE_VALOR = float(500.00)
saques_realizados = 0
saldo = float(1000.00)
data_ultimo_saque = date.today() - timedelta(1)
data_hoje = date.today()
extrato_completo = ""

menu = ' M E N U '.center(40,"-") + """
1 - Extrato
2 - Depósito
3 - Saque
4 - Sair
""" + ''.center(40,"-") + "\n"

def extrato():
    print("\n")
    print(' E X T R A T O '.center(40,"#"))
    print("Não há transação registrada." if not extrato_completo else extrato_completo)
    print(f"Seu saldo é de R$ {saldo:.2f}")
    print(f"Total de saques realizados hoje: {saques_realizados}")
    print(f"Data de emissão: {date.today()}")
    print(' FIM DO EXTRATO '.center(40,"#"))
    print("\n")

def deposito(entrada,saldo,extrato_completo):
    if entrada > 0:
        saldo += entrada
        nova_linha = f"Depósito de R$ {entrada:.2f} Data: {date.today()}\n"
        extrato_completo += nova_linha
        print(f"Depósito de R$ {entrada:.2f} realizado com sucesso!")
        return saldo, extrato_completo
    else:
        print("Depósito com valor inválido!")
        return saldo, extrato_completo
    
def saque(saida,
          saldo,
          LIMITE_SAQUE,
          LIMITE_SAQUE_VALOR,
          saques_realizados,
          data_ultimo_saque,
          data_hoje,
          extrato_completo):
    
    if saida > 0  and LIMITE_SAQUE_VALOR >= saida and saldo >= saida and saques_realizados < LIMITE_SAQUE:

        if data_ultimo_saque != data_hoje:
            saques_realizados = 0
            data_ultimo_saque = date.today()
    
        saldo -= saida
        saques_realizados += 1
        nova_linha = f"Saque de R$ {saida:.2f} Data: {date.today()}\n"
        extrato_completo += nova_linha
        print(f"Saque de R$ {saida:.2f} realizado com sucesso!")
        return saldo, saques_realizados, data_ultimo_saque, extrato_completo

    else:
        print("Saque não autorizado!")
        return saldo, saques_realizados, data_ultimo_saque, extrato_completo



while True:
    print(menu)
    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        extrato()
    elif opcao == 2:
        entrada = float(input("Digite o valor do depósito: "))
        saldo, extrato_completo = deposito(entrada,saldo,extrato_completo)
    elif opcao == 3:
        saida = float(input("Digite o valor do saque: "))
        saldo, saques_realizados, data_ultimo_saque, extrato_completo = saque(saida,saldo,LIMITE_SAQUE,LIMITE_SAQUE_VALOR,saques_realizados,data_hoje,data_ultimo_saque,extrato_completo)
    elif opcao == 4:
        print("Saindo...")
        break
    else:
        print("Opção inválida!")
