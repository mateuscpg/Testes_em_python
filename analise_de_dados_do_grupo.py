'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
 o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.'''

somaid = 0
somahomem = 0
somamulher = 0
while True:
    idade = int(input("Qual a idade? "))
    sexo = str(input("Homem ou mulher? ")).upper().strip()[0]
    if idade >= 18:
        somaid += 1
    if sexo == 'H':
        somahomem += 1
    if sexo == 'M' and idade < 20:
        somamulher +=1
    opc = str(input("Deseja continuar?")).upper().strip()[0]
    if opc == 'N':
        break
print(f"Há {somaid} pessoas com mais de 18 anos")
print(f"Há {somahomem} homens cadastrados")
print(f"Há {somamulher} mulher(es) que tem menos que 20 anos cadastradas")
    

