'''CRIE UMA FUNÇÃO QUE RECEBE UMA OUTRA FUNÇÃO COMO PARÂMENTRO
E RETORNE O VALOR DESSA OUTRA FUNÇÃO EXECUTADA'''

def func1():
    return "Olá mundão"

def mestre(funcao):
    return funcao()

var = mestre(func1)
print(var)

'''CRIE UMA FUNÇÃO QUE RECEBE UMA OUTRA FUNÇÃO COMO PARÂMENTRO
E RETORNE O VALOR DESSA OUTRA FUNÇÃO EXECUTADA. FAÇA A PRIMEIRA
FUNÇÃO EXECUTAR DUAS FUNÇÕES QUE RECEBAM UM NÚMERO DIFERENTE DE ARGUMENTOS'''

def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)

def fala(nome):
    return f'Oi {nome}'

def saudacao(nome, saudacao):
    return f'{saudacao}, {nome}'

var = mestre(fala, 'Mateus')
var2 = mestre(saudacao, 'Mateus', 'Bom dia')
print(var)
print(var2)
