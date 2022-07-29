from random import randrange


pessoas = int(input("Quantas pessoa serão?"))
somaidade = 0
mediaidade = 0
maiorhomem = 0
nomevelho = '' 
totmulher20 = 0
for c in range(1, pessoas + 1):
    print("------{}°Pessoa-------".format(c))
    nome = str(input("Qual o seu nome? ")).strip()
    idade = int(input("Qual a sua idade? "))
    sexo = (input("Sexo [M/F]:")).strip()
    somaidade += idade
    if c == 1 and sexo in 'Mm':
        maiorhomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maiorhomem:
        maiorhomem = idade 
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1

mediaidade = somaidade / pessoas
print ("A média de idade do grupo é de {:.1f} anos.".format(mediaidade))
print ("O homem mais velho tem {} anos e se chama {}.".format(maiorhomem, nomevelho))
print ("Há {} mulher/mulheres com menos de 20 anos de idade.".format(totmulher20))

