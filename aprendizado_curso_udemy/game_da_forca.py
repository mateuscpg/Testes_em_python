import getpass
secret = getpass.getpass("Qual a palavra da forca ?").upper().strip()
digit = []
chances = int(input("Quantas chances você quer dar? "))

while True:
    if chances <= 0:
        print("VOCÊ PERDEU!!!")
        break
    letra = input(f"\nDigite uma letra(VOCÊ SÓ TEM {chances} CHANCES): ").upper().strip()
    if len(letra) > 1:
        print("Só pode digitar uma letra...")
        continue
    digit.append(letra)

    if letra in secret:
        print("Booooa, essa letra está na forca.\n")
    else:
        print("Ah não, essa letra não está na forca.")
        digit.pop()
        chances -= 1

    secret_temp = ''
    for letra_secret in secret:
        if letra_secret in digit:
            secret_temp += letra_secret
        else:
            secret_temp +=' _ ' 
        
    if secret_temp == secret:
        print(f"Parabéns, VOCÊ GANHOU!!! A palavra da forca é {secret}")
        break
    else:
        print(f"A palavra está escrita assim: \n{secret_temp} ")