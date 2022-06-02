'''Faça um programa que gera uma lista 
dos números primos existentes entre 1 e um
número inteiro informado pelo usuário.'''
n = int(input("Digite um número inteiro(que seja maior que 1): "))
lista = []
i = 2
while (i <= n):
    j = 1
    cont = 0
    while (j <= i):
        if (i % j == 0):
            cont += 1
        j += 1   
    if (cont == 2):
        lista.append(i)
    i += 1
print(lista)

                  
   

            
        

        


