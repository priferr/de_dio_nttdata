#for quando sabem o numero de repeticoes ou com objeto iterável

nome = "phoebe"

for letra in nome:
    print(letra.upper())

#range com for - range gera uma sequencia de numeros inteiros no formato range(início, fim, variação)

for numero in range(0,11,2):
    print(numero, end=" \n")

#while pra repetir um bloco de código várias vezes sem um número fixo de vezes que iterará

opcao_escolhida = int(input("digite um código: "))

while opcao_escolhida != 0:
    if opcao_escolhida == 1:
        print("Sacando")
    elif opcao_escolhida == 2:
        print("Extrato")
    else:
        print("exit")
        SystemExit

#break e continue - usados pra parar a iteração e continuar mesmo que tenha atingido o objetivo

while True:
    numero = int(input("digite um numero: "))

    if numero == 0:
        continue
    if numero %2 == 0:
        break
    print(numero)

#questionario
#1 Quais são as estruturas condicionais disponíveis em Python? >if/ elif/ else
#2 comando interromper >break
#3 Range é uma função built-in do Python, ela é usada para produzir uma sequência de números inteiros. >V
#4 O comando while é usado para percorrer um objeto iterável. Faz sentido usar while quando sabemos o número exato de vezes que nosso bloco de código deve ser executado. > F
#5 Qual o comando utilizado para pular um ciclo de iteração dos comando for e while? > continue
#6 Qual a função principal da indentação em um programa Python? >interpretador entende onde comeca e termina um bloco de codigo
