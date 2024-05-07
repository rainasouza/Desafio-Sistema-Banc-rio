menu = """
Digite:

    (1) se você deseja sacar
    (2) se você deseja depositar
    (3) se você deseja visualizar extrato
    (4) se você deseja criar conta
    (5) se você deseja criar um novo usuário

"""

conta = 0
limiteSaque = 3
extrato = ""
contas = []
usuarios = []
agencia = "0001"


def fazerSaque(conta, limiteSaque, extrato):
    saque = int(input("Digite o valor a ser sacado: "))
    if saque > 500:
        print("O limite máximo de saques é 500 reais")
    elif saque > conta:
        print("Você não possui saldo suficiente.")
    else:
        print("Saque feito com sucesso!")
        conta -= saque
        limiteSaque -= 1
        extrato += f"Saque: R$ {saque:.2f}\n"
    return conta, limiteSaque, extrato

def depositar(conta, extrato):
    deposito = int(input("Quanto você deseja depositar? "))
    conta += deposito
    extrato += f"Depósito: R$ {deposito:.2f}\n"
    print("Depósito realizado")
    return conta, extrato

def exibirExtrato(extrato, conta):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nConta: R$ {conta:.2f}")
    print("==========================================")


def criarUsuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrarUsuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")


def filtrarUsuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criarConta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrarUsuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

while True:
    entrada = int(input(menu))
    if entrada == 1:
        conta, limiteSaque, extrato = fazerSaque(conta, limiteSaque, extrato)
    elif entrada == 2:
        conta, extrato = depositar(conta, extrato)
    elif entrada == 3:
        exibirExtrato(extrato, conta)
        numero_conta = len(contas) + 1
        conta = criarConta(agencia, numero_conta, usuarios)
        if conta:
            contas.append(conta)
    elif entrada == 5:
        criarUsuario(usuarios)
    else:
        print("Coloque uma entrada válida")
