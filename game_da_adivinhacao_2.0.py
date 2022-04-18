from random import randint
from time import sleep
comp = randint(0,10)
print("-=-" * 20)
print("Vou pensar em um número entre 0 e 10, tente adivinhar...")
print("-=-" * 20)
palpite = 0
acertou = False
while not acertou:
    jog = int(input("Em que número você está pensando?"))
    palpite += 1
    if jog == comp:
        acertou = True
    else:
        if jog < comp:
            print("Mais... Tente novamente")
        elif jog > comp:
            print("Menos... Tente novamente")

print ("Você GANHOU! PARABÉNS")
print ("Foi preciso {} palpites para você acertar!".format(palpite))
