opc = 'S'
media = 0
soma = 0
qntd = 0
maior = 0 
menor = 0

while opc in 'Ss':
    while True:
        try:
            num = int(input("Digite um número inteiro: "))
            break
        except:
            print("Opção inválida!")
    soma += num
    qntd += 1
    if qntd == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    while True:
        try:
            opc = str(input("Você deseja continuar[s/n]? ")).upper().strip()[0]
            break
        except:
            print("Opção inválida!")


media = soma / qntd
print(f"Você digitou {qntd} e a média desses números é {media}")
print(f"O maior número é {maior} e o menor número é {menor}")


