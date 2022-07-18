import random

print ("JOGO DO PAR OU IMPAR")
vitoria = 0
soma = 0
out = 0
while True:
    valor = int(input("Digite um valor: "))
    jog = str(input("Você escolhe par ou impar? ")).upper().strip()[0]
    print("-"*30)
    comp = random.randint(0,10)
    soma = valor + comp
    print(f"Você jogou {valor} e o computador jogou {comp}, o resultado é {soma} então...")
    if soma % 2:
        out = 'P'
    else:
        out = 'I'

    if jog ==  out:
        print('PARABÉNS, VOCÊ GANHOU')
        print("-"*30)
        vitoria += 1
    else: 
        print('VOCÊ PERDEU!')
        print("-"*30)
        break
print(f'Você ganhou {vitoria} vez(es)')