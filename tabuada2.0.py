while True:
    valor = int(input("\nQuer saber a tabuada de que número?"))
    if valor < 0:
        break
    for c in range (0,11):
        print (f'{valor} x {c} = {valor*c}')
    