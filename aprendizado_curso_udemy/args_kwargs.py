def func(*args, **kwargs):   #args é usada para quando você não souber quantos argumentos
    print(args)              #vai usar. Retorna uma tupla.
    print(kwargs)            #kwargs é usada para você retornar um valor com uma chave(dicionário)

    idade = kwargs.get('idade')    #get está verificando se a chave 'idade' existe.
    if idade is not None:          
        print(f"A idade é: {idade} anos")
    else:
        print("Idade inexistente")

    #print(kwargs['nome'], kwargs['sobrenome'])  #acessa as chaves 'nome' e 'sobrenome' do dicionário.

lista = [1,2,3,4]
lista2 = [5,6,7,8]
func(*lista, *lista2, nome = "Mateus", sobrenome = "Correia")   #Virá um tupla desempacotada da lista e da lista 2
                                                                #e virá um dicionário tendo 'nome' e 'sobrenome' como
                                                                #chave, e 'Mateus' e ' Correia' como valores.
