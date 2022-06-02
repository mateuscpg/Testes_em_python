'''import numpy as np

class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

    def mostrar_no(self):
        print(self.valor)

class Lista_Encadeada:
    def __init__(self):
        self.primeiro = None 

    def insere_inicio(self, valor):
        novo = No(valor)
        novo.proximo = self.primeiro
        self.primeiro = novo

    def mostrar(self):
        if self.primeiro == None:
            print("A lista está vazia")
            return None

        atual = self.primeiro
        while atual != None:
            atual.mostrar_no()
            atual = atual.proximo
        
    def pesquisar (self, valor):
        if self.primeiro == None:
            print("A lista está vazia")
            return None
        
        atual = self.primeiro
        while atual.valor != valor:
            if atual.proximo == None:
                return None
            else:
                atual = atual.proximo
            return atual
    
    def excluir_inicio(self):
        temp = self.primeiro
        if self.primeiro.proximo == None:
            return None
        else:
            self.primeiro = self.primeiro.proximo
            return temp 

    def excluir_posicao(self, valor):
        atual = self.primeiro
        anterior = self.primeiro
        while atual.valor != valor:
            if atual.proximo == None:
                return None
            else:
                anterior = atual
                atual = atual.proximo
            if atual == self.primeiro:
                self.primeiro = self.primeiro.proximo
            else:
                anterior.proximo = atual.proximo
            return atual

lista = Lista_Encadeada()

lista.insere_inicio(1)

lista.primeiro()
lista.mostrar()

lista.insere_inicio(2)
lista.insere_inicio(3)
lista.insere_inicio(4)

lista.mostrar()

lista.excluir_inicio()
'''

import numpy as np

class No:
  def __init__(self, valor):
    self.valor = valor
    self.proximo = None
  
  def mostra_no(self):
    print(self.valor)

class ListaEncadeada:
  def __init__(self):
    self.primeiro = None

  def insere_inicio(self, valor):
    novo = No(valor)
    novo.proximo = self.primeiro
    self.primeiro = novo

  def mostrar(self):
    if self.primeiro == None:
      print('A lista está vazia')
      return None
    
    atual = self.primeiro
    while atual != None:
      atual.mostra_no()
      atual = atual.proximo

  def pesquisa(self, valor):
    if self.primeiro == None:
      print('A lista está vazia')
      return None

    atual = self.primeiro
    while atual.valor != valor:
      if atual.proximo == None:
        return None
      else:
        atual = atual.proximo
    return atual

  def excluir_inicio(self):
    if self.primeiro == None:
      print('A lista está vazia')
      return None
    
    temp = self.primeiro
    self.primeiro = self.primeiro.proximo
    return temp

  def excluir_posicao(self, valor):
    if self.primeiro == None:
      print('A lista está vazia')
      return None
    
    atual = self.primeiro
    anterior = self.primeiro
    while atual.valor != valor:
      if atual.proximo == None:
        return None
      else:
        anterior = atual
        atual = atual.proximo
    
    if atual == self.primeiro:
      self.primeiro = self.primeiro.proximo
    else:
      anterior.proximo = atual.proximo

    return atual

