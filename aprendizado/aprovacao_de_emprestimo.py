from time import sleep
casa = float(input("Qual o valor da casa?"))
sal = float(input("Qual o salário do comprador?"))
anos = int(input("Em quantos anos ele pretende pagar?"))
por = (sal * 30) /100
mensal = casa / (anos * 12) 
print ("PROCESSANDO...") 
sleep(1)
if mensal > por:
    print ("O valor da prestação é de R${:.2f} e excedeu 30% do salário, o empréstimo foi negado".format(mensal))
else: 
    print ("O empréstimo foi aprovado, parabéns!")
