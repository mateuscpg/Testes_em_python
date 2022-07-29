from time import sleep
num = int(input("Digite um número para saber o seu fatorial:"))
c = num
fac = 1
print ('Calculando o fatorial de {}...'. format(num))
sleep(1.3)
while c > 0:
    print ('{}'.format(c), end = '')
    print (' x ' if c > 1 else ' = ', end ='')
    fac *= c
    c -= 1  
print ('{}'.format(fac))

