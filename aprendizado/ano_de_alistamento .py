from datetime import date
atual = date.today().year
ano = int(input("Qual o ano que vc nasceu?"))
idade = atual - ano 
print ('''Você é:
[1] Homem
[2] Mulher''')
opção = int(input("Seu sexo:"))

if opção == 2:
    print("Você não precisa se alistar")
elif opção == 1 and idade == 18:
    print('{:~^50}'.format("~"))
    print ("Quem nasceu em {} tem {} anos em {}".format(ano, idade, atual))
    print("Você já pode se alistar")

elif idade < 18:
    print('{:~^50}'.format("~"))
    saldo = 18 - idade
    print("Não está na hora de você se alistar, falta {} anos para você se alistar".format(saldo))
    saldo2 = atual + saldo
    print ("Seu alistamento sera em {}".format(saldo2))
    
elif idade > 18:
    print('{:~^50}'.format("~"))    
    saldo = idade - 18
    print("Já passou do tempo de você se alistar, você está atrasado em {} anos".format(saldo))
    saldo2 = atual - saldo
    print ("Seu alistamento foi em {}".format(saldo2))
