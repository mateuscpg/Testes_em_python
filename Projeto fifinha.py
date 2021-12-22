import random
print ('{:-^50}'.format('Bem vindo ao Fifinha'))
jog = int(input("Quantos jogadores serão?"))
i = 0 
lista = []
while i < jog:
    lista.insert(i, input("Digite o nome do jogador:"))
    i += 1
    
print ("{:=^50}".format("PARTIDAS:"))

esco = random.choice(lista)
esco2 = random.choice(lista)
esco3 = random.choice(lista)

while esco == esco2 == esco3:
  esco = random.choice(lista)
  esco2 = random.choice(lista)
  esco3 = random.choice(lista)

print ("{} x {}".format(esco, esco2))
print ("{} x {}".format(esco, esco3))
print ("{} x {}".format(esco2, esco))
print ("{} x {}".format(esco2, esco3))
print ("{} x {}".format(esco3, esco))
print ("{} x {}".format(esco3, esco2))

