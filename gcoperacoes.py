"""
(c) 2019-2021 Nurul-GC
"""
from math import *


class Operacoes:
    def __init__(self):
        self.valor1 = 0
        self.valor2 = 0

    def soma(self):
        if (self.valor1 and self.valor2) == 0:
            return None
        return self.valor1+self.valor2

    def subtracao(self):
        if (self.valor1 and self.valor2) == 0:
            return None
        return self.valor1-self.valor2

    def multiplicacao(self):
        if (self.valor1 and self.valor2) == 0:
            return None
        return self.valor1*self.valor2

    def divisao(self):
        if (self.valor1 and self.valor2) == 0:
            return None
        return self.valor1/self.valor2

    def expoente(self):
        if self.valor1 == 0:
            return exp(self.valor2)
        elif self.valor2 == 0:
            return exp(self.valor1)
        else:
            if (self.valor1 and self.valor2) == 0:
                return None
            return exp(self.soma())

    def expoente_neg(self):
        if self.valor1 == 0:
            return expm1(self.valor2)
        elif self.valor2 == 0:
            return expm1(self.valor1)
        elif (self.valor1 and self.valor2) == 0:
            return None
        else:
            return expm1(self.soma())

    def raiz2(self):
        if self.valor1 == 0:
            return sqrt(self.valor2)
        elif self.valor2 == 0:
            return sqrt(self.valor1)
        elif (self.valor1 and self.valor2) == 0:
            return None
        else:
            return sqrt(self.soma())

    def modulo(self):
        if (self.valor1 and self.valor2) == 0:
            return None
        return fmod(self.valor1, self.valor2)

    def logo(self):
        if self.valor1 == 0:
            return log2(self.valor2)
        elif self.valor2 == 0:
            return log2(self.valor1)
        elif (self.valor1 and self.valor2) == 0:
            return None
        else:
            return log2(self.soma())
