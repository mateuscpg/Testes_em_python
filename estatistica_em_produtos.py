'''Crie um programa que leia o nome e o preço de vários produtos.
 O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.'''
totgast = 0
prod1000 = 0
menor = 0
cont = 0
barato = ''
while True:
    prod = str(input("Nome do produto: "))
    preco = float(input("Preço do produto: R$"))
    cont +=1 
    totgast = totgast + preco
    if preco >= 1000:
        prod1000 += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = prod
    else:
        if preco < menor:
            menor = preco
            barato = prod 

    opc = str(input("Deseja continuar?")).upper().strip()[0]
    if opc == "N":
        break
print("-"*50)
print(f"O total da compra foi R${totgast:.2f}")
print(f"Temos {prod1000} produto(s) que custa(am) mais de R$1000")
print(f"O menor produto cadastrado foi o/a {barato} que custa R${menor:.2f}")