from datetime import date
atual = date.today().year
ano = int(input("Qual o ano que vc nasceu?"))
idade = atual - ano 

if idade <= 9:
    print("Você tem {} anos, sua categoria é MIRIM!".format(idade))
elif idade >= 10 and idade <= 14:
    print("Você tem {} anos, sua categoria é INFANTIL!".format(idade))
elif idade >= 15 and idade <=19:
    print("Você tem {} anos, sua categoria é JÚNIOR".format(idade))
elif idade == 20:
    print("Você tem {} anos, sua categoria é SÊNIOR".format(idade))
elif idade > 20:
    print("Você tem {} anos, sua categoria é MASTER".format(idade))
