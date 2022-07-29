s = 0
for c in range (0, 7):
    n = int(input("Digite um número:"))
    n1 = n % 2
    if n1 == 0:
        s += n
print("A soma dos pares é {}".format(s))


