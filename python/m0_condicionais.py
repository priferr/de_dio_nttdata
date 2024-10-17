#else if/ elif
MAIOR_IDADE = 18
IDADE_ESPECIAL = 17
#constantes representadas por maiusculas

idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de 18, pode tirar a CHN.")

if idade < MAIOR_IDADE:
    print("Não tem idade pra tirar a CNH.")


if idade >= MAIOR_IDADE:
    print("Maior de 18, pode tirar a CHN.")
else:
    print("Não tem idade pra tirar a CNH.")


if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CHN.")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teóricas, mas não pode fazer aulas práticas.")
else:
    print("Ainda não pode tirar a CNH.")


 #condicionais aninhados If dentro de if
#if:
#        if:
#        elif
#elif
#        if:
#        else:
             
conta_normal = False
conta_universitaria = False
conta_especial = True

saldo = 2000
saque = 1500
cheque_especial = 450

if conta_normal:

    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial!")
    else:
        print("Não foi possivel realizar o saque, saldo insuficiente!")

elif conta_universitaria:

    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")

elif conta_especial:
    print("Conta especial selecionada!")

else:
    print("Sistema não reconheceu seu tipo de conta, entre em contato com o seu gerente.")


#condicionais ternários: if escrito em 3 partes em uma unica linha

status = "sucesso" if saldo >= saque else "Falha"
