'''SE QUISER GERAR UM CPF ALEATÓRIO:
from random import randint

cpf = str(randint(100000000, 999999999))'''



while True:
    cpf = str(input("Qual o seu CPF? "))
    if cpf.__len__() == 11:
        print(cpf[0:3],cpf[3:6], cpf[6:9], sep='.',end= '-')
        print(cpf[9:11])
        break
    else: 
        print("CPF inválido")
novo_cpf = cpf[:9]          #Elimina dois últimos dígitos do CPF
reverso = 10                #Conta reverso no for
tot = 0 
for i in range (19):
    if i > 8:                             #Primeiro índice vai de 0 a 9
        i -= 9                             #São os 9 primeiros dígitos do CPF

    tot += int(novo_cpf[i]) * reverso       #Valor total da multiplicação

    reverso -= 1                             #Decrementa o contador 'reverso'
    if reverso <2:
        reverso = 11
        d = 11 - (tot % 11)

        if d > 9:                           #Se o dígito fo > que 9 o valor é 0
            d = 0
        tot = 0                              
        novo_cpf += str(d)                  #Concatena o digito gerado no novo CPF

if cpf == novo_cpf:
    print("CPF válido")
else:
    print("CPF inválido")


    



        

