from time import sleep
valor1 = int(input('Digite o primeiro valor:'))
valor2 = int(input('Digite o segundo valor:'))
esco = 0
while esco != 5:
    print ('''    [1] Soma
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa''')
    esco = int(input('Escolha sua opção:'))
    if esco == 1:
        soma = valor1 + valor2
        print ('{} + {} = {}'.format(valor1, valor2, soma))
    elif esco == 2:
        mult = valor1 * valor2
        print ('{} x {} = {}'.format(valor1, valor2, mult))
    elif esco == 3:
        if valor1 > valor2:
            maior = valor1
        else:
            maior = valor2
        print ('O maior valor entre {} e {} é {}'.format(valor1, valor2, maior))
    elif esco == 4:
        print ('Informe os números novamente')
        valor1 = int(input('Digite o primeiro valor:'))
        valor2 = int(input('Digite o segundo valor:'))
    elif esco == 5:
        print('Finalizando...')
    else:
        print('Opção inválida')
    print ("=-="*15)
    sleep(1.8)
print("Fim do programa, volte sempre!")
    
        

        