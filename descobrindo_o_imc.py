 #CALCULANDO O IMC DA GALERA
nome = input ('Qual o seu nome?')
idade = input ('Qual a sua idade?')
a = float(input ('Qual a sua altura?'))
p = float(input ('Qual o seu peso?'))
imc1 = float (a**2)
imc2 = float (p/imc1)
if imc2 < 18.5:
    print("{}, seu IMC é {:.3f}, você está abaixo do peso".format(nome,imc2))
elif imc2 >= 18.5 and imc2 <= 24.9:
    print("{}, seu IMC é {:.3f}, seu peso está normal.".format(nome, imc2))
elif imc2 >= 25.0 and imc2 <= 29.9:
    print ("{}, seu IMC é {:.3f}, você está acima do peso.".format(nome, imc2))
elif imc2 >= 30 and imc2 <= 40:
    print ("{}, seu IMC é {:.3f}, você está em obesidade".format(nome, imc2))
elif imc2 > 40:
    print("{}, seu IMC é {:.3f}, você está em obesidade mórbida".format(nome, imc2))
