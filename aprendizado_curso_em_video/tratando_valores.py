''' Crie um programa que leia vários números inteiros pelo teclado.
 O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles 
(desconsiderando o flag).'''
num = cont = soma = 0
num = int(input("Digite um número [para sair digite '999']: "))
while num != 999:
    soma = soma + num
    cont = cont + 1
    num = int(input("Digite um número [para sair digite '999']: "))
print(f"Você digitou {cont} números e a soma deles é {soma} ")
    
