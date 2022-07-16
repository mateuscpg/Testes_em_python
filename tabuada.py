opc = int(input("Quer saber a tabuada de qual valor? "))
while opc > 0:
    for i in range(0,11):
        print(f"{opc} x {i} = {opc*i} ")
    print("--------------------")    
    opc = int(input("Quer saber a tabuada de qual valor? "))
print("Fim do programa!")