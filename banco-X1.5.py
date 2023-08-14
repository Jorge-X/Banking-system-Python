import time
import textwrap
# Esse é o script que simula um banco., ele está escrito em python
# ele te dá um menu simples com 4 opções. Depositar, sacar, exibir extrato e sair
# Esse banco tem limite diario de 3 saque.
# Ele não aceita o saque de valores acima de R$ 500.00
# o limite de saque é para manter a segurança dos usuarios.
# E esse primeiro banco tem um usuario fixo.
# ultilizo a biblioteca time para adicionar tempo a algumas telas.


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

    elif excedeu_limite:
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

    elif excedeu_saques:
        print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")

    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def menu(): 
    menu_text = '''================_Banco_================
    seja bem vindo!

    [1] Nova conta 
    [2] Novo usuário 
    [3] Listar contas
    [4] Exibir extrato
    [5] Depositar
    [6] Sacar
    [7] Sair

    =======================================
    digite aqui a opcao desejada: '''
    return input(textwrap.dedent(menu_text))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == '1':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == '2':
            criar_usuario(usuarios)

        elif opcao == '3':
            listar_contas(contas)

        elif opcao == '4':
            print("\n================ EXTRATO ================")
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("==========================================\n")

        elif opcao == '5':
            valor_deposito = float(input("valor que deseja depositar: "))
            if valor_deposito > 0:
                saldo += valor_deposito
                extrato += f"Deposito: +R$ {valor_deposito:.2f}\n"
                print("valor depositado com sucesso!\n")
            else:
                print('''
                    Esse valor não pode ser depositado\n!
                    ''')

        elif opcao == '6':
            saque_desejado = float(input("valor que deseja sacar: \n"))
            if saque_desejado <= limite and LIMITE_SAQUES >= 1 and saque_desejado <= saldo and saque_desejado <= limite and saque_desejado >= 1:
                LIMITE_SAQUES -= 1
                saldo -= saque_desejado
                extrato += f"Saque: -R$ {saque_desejado:.2f}\n"
                time.sleep(1)
                print(f'''Saque de {saque_desejado:.2f} efetuado com sucesso!\nVocê ainda tem {LIMITE_SAQUES} saque(s) diário(s).\n''')
                time.sleep(2)
                print("seu extrato será exibido aguarde...")
                time.sleep(4)
                print(extrato)
                print("voltando para o menu...")
                time.sleep(3)
            elif saque_desejado <= 0:
                print("@@@ Valor invalido @@@")
                time.sleep(5)
                print("Lamento, mas você não pode sacar um valor nulo ou negativo.")
                time.sleep(3)
                print("Voltando para o menu, aguarde...\n")
                time.sleep(3)
            else: 
                print(f"\nLamento, você não pode sacar esse valor.\nVocê tem {LIMITE_SAQUES} saque(s) diário(s).\nTalvez você tenha excedido algum limite")
                time.sleep(5)
                print("Voltando para o menu, aguarde...\n")
                time.sleep(3)

        elif opcao == '7':
            print("Saindo... Aguarde!")
            time.sleep(5)
            break 

        else:
            print("Lamento, opção inválida.\nVamos tentar novamente\nVocê está sendo redirecionado para o menu...")
            time.sleep(5)

# Resto das funções...

main()

