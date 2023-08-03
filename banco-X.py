import time
# Esse é o script que simula um banco., ele está escrito em python
# ele te dá um menu simples com 4 opções. Depositar, sacar, exibir extrato e sair
# Esse banco tem limite diario de 3 saque.
# Ele não aceita o saque de valores acima de R$ 500.00
# o limite de saque é para manter a segurança dos usuarios.
# E esse primeiro banco tem um usuario fixo.
# ultilizo a biblioteca time para adicionar tempo a algumas telas.

menu = '''================_Banco_================
seja bem vindo!

[1] Depositar
[2] Sacar
[3] Exibir extrato
[4] Sair

=======================================
digite aqui a opcao desejada: '''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    if int(opcao) == 1:
            valor_deposito = float(input("valor que deseja depositar: "))
            if valor_deposito > 0:
                saldo += valor_deposito
                extrato += f"Deposito: +R$ {valor_deposito:.2f}\n"
                print("valor depositado com sucesso!\n")
            else:
                print('''
                      Esse valor não pode ser depositado\n!
                      ''')
                
    elif int(opcao) == 2:
        saque_desejado = float(input("valor que deseja sacar: "))
        if saque_desejado <= limite and LIMITE_SAQUES >= 1 and saque_desejado <= saldo and saque_desejado <= limite:
            LIMITE_SAQUES -= 1
            saldo -= saque_desejado
            extrato += f"Saque: -R$ {saque_desejado:.2f}\n"
            print(f'''Saque de {saque_desejado:.2f} efetuado com sucesso!\nVocê ainda tem {LIMITE_SAQUES} saque(s) diario(s).\n''')
            print(extrato)

        else: 
            print(f"Lamento, vocẽ não pode sacar esse valor.\nVocê tem {LIMITE_SAQUES} saque(s) diario(s).\nTalvez você tenha excedido algum limite")
            time.sleep(5)
            print("Voltando para menu, aguarde...")
            time.sleep(3)

    elif int(opcao) == 3:
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================\n")

    elif int(opcao) == 4:
        print("Saindo... Aguarde!")
        time.sleep(5)
        break 

    else:
        print("Lamento, opção invalida.\nVamos tentar novamente\nVocê está sendo redirecionado para o menu...")
        time.sleep(5)