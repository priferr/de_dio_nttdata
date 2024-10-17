#operadores aritméticos -> igual, menos, dividido, remainder, elevado a potência
a = 5
b = 4

print(a+b)
print(a-b)
print(a/b)
print(a//b)
print(a*b)
print(a%b)
print(a**b)

x = (10 % 5) + (8 % 2)
y = (10/2) + (25 * 2) - (3 ** 2)

print(x)
print(y)

#operadores de comparação -> maior que, menor, menor ou igual, diferente etc
saldo = 200
saque = 100
print(saque)

print(saldo > saque)
print(saldo != saque)
print(saldo <= saque)

saque %= 4
print(saque)
#resultado zero pq saque dividido por 4 tem resto 0

#operadores lógicos -> and, or
saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp)

exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp_2)

conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque

#operadores de identidade -> is, is not
saldo = 1000
limite = 1000

print(saldo is limite)
print(saldo is not limite)

#operadores de associação -> in, not in
frutas = ["limao", "uva"]
curso = "Curso de python"

print("laranja" not in frutas)
print("limao" in frutas)
print("Python" in curso)

x = (22 - 10) * 3
print(x)
