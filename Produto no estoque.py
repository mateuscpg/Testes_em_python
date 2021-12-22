#Escreva um programa que leia do teclado o
#código de uma peça e a quantidade disponível no estoque. Esses dois dados de
#entrada são números inteiros. Acrescente o par código:quantidade
#em um dicionário apenas se o código não estiver presente.
#Caso esteja, dê uma mensagem informando
#essa situação e descarte os dados. O laço termina quando for fornecido 0 para o
#código. Exibir na tela os dados do dicionário, um membro por linha.

i = 1
estoque = {}
while i != 0:
    cod1 = int(input("Qual o código do produto?"))
    if cod1 == 0:
        print ("Não há o produto no estoque com esse código")
        continue
    if cod1 in estoque:
        print ("O produto já está cadastrado")
        continue
    quant = int(input("Qual a quantidade que tem na loja?"))
    estoque[cod1] = quant
    i = int(input("Digite 0 para sair ou outro número para contínuar:"))
    for x in estoque:
        print("Código do produto:{}; Quantidade: {}".format(x, estoque[x]))
    



    





    
    









