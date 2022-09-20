from turtle import Vec2D


l1 = [1,2,3,4,5,6,7,8,9]
ex1 = [variavel for variavel in l1]
print(ex1)
print()

ex2 = [v* 2 for v in l1]
print(ex2)                    #Multiplica cada valor de l1 por 2
print()

ex3 = [(v, v2)for v in l1 for v2 in range(3)]
print(ex3)                                       #Pega cada valor de l1 e mostra ele 3 vezes
print()

l2 = ['Mateus', 'Lucas', 'Zete']
ex4 = [v.replace('a', '@').upper() for v in l2]    #Troca a letra 'a' por '@' de l2 e bota tudo em maiúsculo
print(ex4)
print()

tupla = (
    ('chave', 'valor'),
    ('chave2', 'valor2')
)

ex5 = [(y,x)for x,y in tupla]                #Inverte os lugares de chave e valor
ex5 = dict(ex5)                              #Transforma a tupla em dicionário
print(ex5)          
print()                        

l3 = list(range(100))
ex6 = [v for v in l3 if v % 3 == 0 if v % 8 == 0]
print(ex6)          
print()      

ex7 = [v if v % 3 == 0 else "__" for v in l3]
print(ex7)          
print()      
