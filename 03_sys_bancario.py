#inserir novas opções, usar dicionário e checagem em lista

menu = """"
[1] Depósito
[2] Saque
[3] Extrato
[4] Novo Cliente
[5] Nova Conta
[0] Sair

Escolha a opção desejada: """

saldo = 0
limite = 500
extrato = " "
numero_saques = 0
LIMITE_SAQUES = 3
agencia = "0001"
conta = 0
clientes = [
    {"nome": "Priscilla", "cpf": "04651806554"}
]

while True:
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Valor do Depósito: "))

        if valor < 0:
            print("Valor inválido, operação não realizada.")
        else:
            saldo += valor
            extrato += f"Depósito R${valor:.2f}\n"

    elif opcao == "2":
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

    elif opcao == "3":
        print(extrato)
        print(f"\n Saldo atual:  R${saldo:.2f}")

    elif opcao == "4":
            cpf = input("Digite apenas os números do seu CPF: ")
            cpf_existente = False
            for cliente in clientes:
                 if cliente["cpf"] == cpf:
                      cpf_existente = True
                      break

            if cpf_existente:
                 print("Cliente já cadastrado") 
            else:
                 nome = input("Nome completo: ")
                 clientes.append({"nome": nome, "cpf": cpf})
                 print(f"\n Cliente {nome} cadastrado com sucesso!")

    elif opcao == "5":
            cpf = input("Digite o CPF (apenas números): ")
            cpf_existente = False
            for cliente in clientes:
                 if cliente["cpf"] == cpf:
                      cpf_existente = True
                      break

            if cpf_existente:
                 print("Cliente já cadastrado") 
            else:
                 conta += 1
                 print(f"\n Conta {conta} na Agência {agencia} criada com sucesso!")

    elif opcao == "0":
        break

    else:
            print("Operação não realizada - verifique os dados e reinicie o processo.")
