import numpy as np

class Fila:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.inicio = 0
        self.final = -1
        self.numeroElementos = 0
        self.valores = np.empty(self.capacidade, dtype=dict)

    def filaVazia(self):
        return self.numeroElementos == 0

    def filaCheia(self):
        return self.numeroElementos == self.capacidade

    def enfileirar(self, valor):
        if self.filaCheia():
            print('A fila está completa')
        else:
            self.valores[self.numeroElementos] = valor
            self.numeroElementos += 1

    def desenfileirar(self):
        if self.filaVazia():
            print('A fila está vazia')
        else:
            for x in range(self.numeroElementos - 1):
                temp = self.valores[x + 1]
                self.valores[x + 1] = None
                self.valores[x] = temp
            self.numeroElementos -= 1

    def primeiro(self):
        if self.filaVazia():
            return -1
        else:
            return self.valores[self.inicio]