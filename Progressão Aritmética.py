print ("="*20)
print ("10 TERMOS DE UM PA")
print ("="*20)

prim = int(input("Primeiro termo:"))
razão = int(input("Razão:"))
décimo = prim + (10 - 1) * razão

for c in range (prim, décimo, razão):
    print ('{}'.format (c), end = "->")
print ("ACABOU")