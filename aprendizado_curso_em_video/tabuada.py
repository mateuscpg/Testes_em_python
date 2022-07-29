while True:
    opc = int(input("Quer saber a tabuada de qual valor? "))
    if opc < 0:
        break
    for i in range(0,11):
        print(f"{opc} x {i} = {opc*i} ")
    print("-"*30)
print("Fim do programa!")