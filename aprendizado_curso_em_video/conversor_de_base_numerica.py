num = int(input("Digite um número inteiro:"))
print ('''Escolha uma das bases para a conversão:
[1] Converter para Binário
[2] Converter para Octal
[3] Converter para Hexadecimal''')
opção = int(input("Sua opção:"))
if opção == 1:
    print("{} convertido para binário é {}".format(num, bin(num)[2:]))
elif opção == 2:
    print("{} convertido em octal é {}".format(num, oct(num)[2:]))
elif opção == 3:
    print("{} convertido para hexadecimal é {}".format(num, hex(num)[2:]))
else:
    print("Número inválido, só pode escolher as opções 1, 2 e 3.")
