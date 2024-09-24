class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class Conta:
    def __init__(self, numero, agencia, saldo=0):
        self.numero = numero
        self.agencia = agencia
        self.saldo = saldo
        self.limite = 500
        self.extrato = ""

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato += f"Depósito R${valor:.2f}\n"
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo and valor <= self.limite:
            self.saldo -= valor
            self.extrato += f"Saque R${valor:.2f}\n"
        else:
            print("Valor de saque inválido ou saldo insuficiente.")


clientes = []

menu = """
[1] Depósito
[2] Saque
[3] Extrato
[4] Novo Cliente
[5] Nova Conta
[0] Sair
Escolha a opção desejada: """

def selecionar_conta(cliente):
    if len(cliente.contas) > 1:
        print("Contas disponíveis:")
        for i, conta in enumerate(cliente.contas):
            print(f"[{i}] Conta {conta.numero}, Agência {conta.agencia}, Saldo: R${conta.saldo:.2f}")
        index_conta = int(input("Escolha o número da conta desejada: "))
        if 0 <= index_conta < len(cliente.contas):
            return cliente.contas[index_conta]
        else:
            print("Opção inválida. Selecionando a primeira conta por padrão.")
            return cliente.contas[0]
    else:
        return cliente.contas[0]

while True:
    opcao = input(menu)

    if opcao == "1":
        cpf = input("Digite o CPF do cliente: ")
        cliente_encontrado = next((cliente for cliente in clientes if cliente.cpf == cpf), None)
        
        if cliente_encontrado:
            conta = selecionar_conta(cliente_encontrado)
            valor = float(input("Valor do depósito: "))
            conta.depositar(valor)
        else:
            print("Cliente não encontrado.")

    elif opcao == "2":
        cpf = input("Digite o CPF do cliente: ")
        cliente_encontrado = next((cliente for cliente in clientes if cliente.cpf == cpf), None)
        
        if cliente_encontrado:
            conta = selecionar_conta(cliente_encontrado)
            valor = float(input("Valor do saque: "))
            conta.sacar(valor)
        else:
            print("Cliente não encontrado.")

    elif opcao == "3":
        cpf = input("Digite o CPF do cliente: ")
        cliente_encontrado = next((cliente for cliente in clientes if cliente.cpf == cpf), None)
        
        if cliente_encontrado:
            conta = selecionar_conta(cliente_encontrado)
            print(f"Extrato: \n{conta.extrato}")
            print(f"Saldo atual: R${conta.saldo:.2f}")
        else:
            print("Cliente não encontrado.")

    elif opcao == "4":
        nome = input("Nome completo: ")
        cpf = input("CPF: ")
        cliente_existente = next((cliente for cliente in clientes if cliente.cpf == cpf), None)
        
        if cliente_existente:
            print("Cliente já cadastrado.")
        else:
            novo_cliente = Cliente(nome, cpf)
            clientes.append(novo_cliente)
            print(f"Cliente {nome} cadastrado com sucesso.")

    elif opcao == "5":
        cpf = input("Digite o CPF do cliente para adicionar uma conta: ")
        cliente_encontrado = next((cliente for cliente in clientes if cliente.cpf == cpf), None)
        
        if cliente_encontrado:
            numero_conta = len(cliente_encontrado.contas) + 1
            nova_conta = Conta(numero=numero_conta, agencia="0001")
            cliente_encontrado.adicionar_conta(nova_conta)
            print(f"Conta {numero_conta} criada com sucesso para o cliente {cliente_encontrado.nome}.")
        else:
            print("Cliente não encontrado.")

    elif opcao == "0":
        break

    else:
        print("Opção inválida.")
