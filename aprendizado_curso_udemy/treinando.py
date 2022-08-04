'''while True:
    cpf = str(input("Qual o seu CPF? "))
    
    if cpf.__len__() == 11:
        print('CPF CADASTRADO'.center(35, '='))
        print(cpf[0:3],cpf[3:6], cpf[6:9], sep='.',end= '-')
        print(cpf[9:11])
        break
    else: 
        print("CPF inválido")'''
l1 = ['String', True, 10, 10.5]

for elem in l1:
    print(f'O tipo de {elem} é {type(elem)}')
