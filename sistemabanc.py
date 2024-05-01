menu = """
Digite:

    (1) se você deseja sacar
    (2) se você deseja depositar
    (3) se você deseja visualizar extrato

"""
conta = 0
limiteSaque = 3
extrato = ""

while True:

    entrada = int(input(menu))


    if entrada == 1:
        saque = int(input("Digite o valor a ser sacado: "))
        if saque > conta:
            print("Você não possui saldo suficiente.")

        elif saque <= conta:
            print("Saque feito com sucesso!")
            conta -= saque
            limiteSaque -= 1
            extrato += f"Saque: R$ {saque:.2f}\n"

        elif saque > 500 :
            print("O limite máximo de saques é 500 reais")

        elif limiteSaque == 0:
            print("Você excedeu o limite máximo de saques diários. Só podem ser realizados 3 saques por dia.")


    elif entrada == 2:
        deposito = int(input("Quanto você deseja depositar? "))
        conta += deposito
        extrato += f"Depósito: R$ {deposito:.2f}\n"
        print("Depósito realizado")
    
    elif entrada == 3:
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nConta: R$ {conta:.2f}")
        print("==========================================")

    else:
        print("Coloque uma entrada válida")
    
