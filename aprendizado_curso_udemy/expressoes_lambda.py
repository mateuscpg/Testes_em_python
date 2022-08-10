'''EXPRESSÕES LAMBDA'''

a = lambda x,y: x*y
print(a(5,5))
#OU
print(a(int(input("Digite o primeiro valor: ")),int(input("Digite outro valor: "))))

print('-'*50)

lista = [
    ['p1', 12],
    ['p2', 4],
    ['p3', 20],
    ['p4', 7],
]

lista.sort(key= lambda item: item[1], reverse=True)
print(lista)
#OU
print(sorted(lista, key=lambda item: item[1], reverse=True))