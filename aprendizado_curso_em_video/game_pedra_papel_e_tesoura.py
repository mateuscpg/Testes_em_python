from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print ('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
print ("-="*11)
jogador = int(input("Qual a sua jogada?"))

print ("JO")
sleep(0.5)
print ("KEN")
sleep(0.5)
print ("PO")
sleep(0.5)

print ('-='*11)
print ("Você jogou {}".format(itens[jogador]))
print ("O computador jogou {}".format(itens[computador]))
print ('-='*11)

sleep(1)

if computador == 0: #Computador jogou pedra
    if jogador == 0:
        print("EMPATE!")
    elif jogador == 1:
        print ("VOCÊ GANHOU!")
    elif jogador == 2:
        print (" VOCÊ PERDEU!")
    else:
        print ("JOGADA INVÁLIDA!")

elif computador == 1: #Computador jogou papel
    if jogador == 0:
        print ("VOCÊ PERDEU!")
    elif jogador == 1:
        print ("EMPATE!")
    elif jogador == 2:
        print ("VOCÊ GANHOU!")
    else:
        print ("JOGADA INVÁLIDA!")

   
elif computador == 2: #Computador jogou tesoura
    if jogador == 0:
        print (" VOCÊ GANHOU!")
    elif jogador == 1:
        print ("VOCÊ PERDEU!")
    elif jogador ==2:
        print (" JOGADA INVÁLIDA!")
    else:
        print ("JOGADA INVÁLIDA!")

