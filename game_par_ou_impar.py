import random

print ("JOGO DO PAR OU IMPAR")
vitoria = 0
soma = 0
while True:
    valor = int(input("Digite um valor: "))
    jog = str(input("Você escolhe par ou impar? ")).upper().strip()[0]
    comp = random.randint(0,10)
    soma = jog + comp
    if soma % 2:
        valor = 'P'
    else:
        valor = 'I'

    if jog == valor:
        print('PARABÉNS, VOCÊ GANHOU')
        vitoria += 1
    else: 
        print('VOCÊ PERDEU!')
        break
print(f'Você ganhou {vitoria} vezes')