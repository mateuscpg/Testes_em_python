from time import sleep
import random

opc = int(input('''Pronto(a) para começar? 
[1] Sim
[2] Não
'''))

if opc == 1:
    lista = ["Netflix", "Prime", "HBO", "GloboPlay", "Disney", "Star+"]
    stream = random.choice(lista)
    print("-----------ESCOLHA DA STREAMING-----------\n")
    sleep(0.8)
    print("A streaming será: {}\n".format(stream))

    lista1 = ["Ação", "Aventura", "Comédia", "Drama", "Fantasia", "Ficção científica", "Musical", "Romance", "Suspense", "Família"]
    filme = random.choice(lista1)
    print("-----------ESCOLHA DA CATEGORIA-----------\n")
    sleep(0.8)
    print("A categoria do filme será: {}\n".format(filme))

    alfabeto = ["A","B","C","D","E","F","G","H","I","J","L","M","N","O","P","Q","R","S","T","U","V","Z"]
    print("-----------ESCOLHA DA LETRA-----------\n")
    sleep(0.8)
    letra = random.choice(alfabeto)
    print("A letra é: {}\n".format(letra))
    print("Bom filme :)")
elif opc == 2:
    print("Beleza moral, vai fazer outra coisa então!")

