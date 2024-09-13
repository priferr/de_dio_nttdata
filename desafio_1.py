menu = """"
[0] Depósito
[1] Saque
[2] Extrato
[3] Sair

Escolha a opção desejada: """

saldo = 0
limite = 500
extrato = " "
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "0":
        valor = float(input("Valor do Depósito: "))

        if valor < 0:
            print("Valor inválido, operação não realizada.")
        else:
            saldo += valor
            extrato += f"Depósito R${valor:.2f}\n"

    elif opcao == "1":
        valor = float(input("Valor do Saque: "))

        if numero_saques >= 3:
            print("Opção inválida, operação não realizada.")
        elif valor < 0:
            print("Valor inválido, operação não realizada.")
        elif valor > 500:
             print(f"Valor acima do limite de R${limite}, operação não realizada.")
        elif valor > saldo:
            print(f"Valor inválido, saldo atual de R${saldo}, operação não realizada.")
        elif valor > 0:
            saldo -= valor
            numero_saques += 1
            extrato += f"Saque R${valor:.2f}\n"
        else:
            print("Operação não realizada - verifique os dados e reinicie o processo.")

    elif opcao == "2":
        print(extrato)
        print(f"\n Saldo atual:  R${saldo:.2f}")

    elif opcao == "3":
        break

    else:
            print("Operação não realizada - verifique os dados e reinicie o processo.")