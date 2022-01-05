print ("="*20)
print ("10 TERMOS DE UM PA")
print ("="*20)

print (''' Você quer saber pelo:
[1] FOR
[2] WHILE''')
op = int(input('Sua opção:'))

if op == 1:
    prim = int(input("Primeiro termo:"))
    razão = int(input("Razão:"))
    décimo = prim + (10 - 1) * razão
    for c in range (prim, décimo, razão):
        print ('{}'.format (c), end = " -> ")
    print ("ACABOU")
    
elif op == 2:
    prim = int(input("Primeiro termo:"))
    razão = int(input("Razão:"))
    termo = prim
    cont = 1
    total = 0
    esco = 10
    while esco != 0:
        total += esco
        while cont <= total:
            print ('{}'.format (termo), end = " -> ")
            termo += razão
            cont += 1
        print ('PAUSA')
        esco = int(input('Quantos termos você quer mostrar a mais?'))  

print ("Progressão finalizada! Foi mostrado {} termos".format(total))