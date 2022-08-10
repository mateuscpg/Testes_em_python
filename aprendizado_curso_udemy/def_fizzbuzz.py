'''Exercício FizzBuzz'''

def funcao(n1):
    if n1 % 3 == 0 and n1 % 5 ==0:
        return f'FizzBuzz, {n1} é divisível por 3 e por 5'
    if n1 % 3 == 0:
        return f'Fizz, {n1} é divisível por 3'
    if n1 % 5 == 0:
        return f'Buzz, {n1} é divisível por 5'
    return f'{n1} não é divisível por 3 e nem por 5'

from random import randint

for i in range(50):
    random = randint(1,50)
    print(funcao(random))
