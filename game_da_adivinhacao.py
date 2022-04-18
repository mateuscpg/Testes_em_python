from random import randint
from time import sleep
comp = randint(0,5)
print("-=-" * 20)
print("Vou pensar em um número entre 0 e 5, tente adivinhar...")
print("-=-" * 20)
jog = int(input("Em que número você está pensando?"))
print("PROCESSANDO...")
sleep (2)
if jog == comp:
    print("Você venceu, eu pensei no número {}".format(comp))
else:
    print("Você perdeu, eu pensei no número {}".format(comp))
