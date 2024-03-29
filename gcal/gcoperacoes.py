"""
(c) 2019-2021 Nurul-GC
"""
from math import *


def isempty(_str: str) -> bool:
    if _str.isspace() or len(_str) == 0:
        return True
    return False


class Operacoes:
    def __init__(self, valor1=0, valor2=0):
        self.valor1 = valor1
        self.valor2 = valor2

    def soma(self):
        return self.valor1 + self.valor2

    def subtracao(self):
        return self.valor1 - self.valor2

    def multiplicacao(self):
        return self.valor1 * self.valor2

    def divisao(self):
        if self.valor1 == 0 and self.valor2 == 0:
            return None
        try:
            return self.valor1 / self.valor2
        except ZeroDivisionError:
            return None

    def expoente(self):
        return pow(self.valor1, self.valor2)

    def expoente_neg(self):
        if self.valor1 and not self.valor2:
            return pow(self.valor1, -1)
        elif self.valor2 and not self.valor1:
            return pow(self.valor2, -1)
        return pow(self.soma(), -1)

    def raiz_quad(self):
        if self.valor1 and not self.valor2:
            return sqrt(self.valor1)
        if self.valor2 and not self.valor1:
            return sqrt(self.valor2)
        return sqrt(self.soma())

    def modulo(self):
        if (self.valor1 and self.valor2) == 0:
            return None
        return fmod(self.valor1, self.valor2)

    def logaritmo(self, _base):
        if self.valor1 == 0:
            return log(self.valor2, _base)
        elif self.valor2 == 0:
            return log(self.valor1, _base)
        elif (self.valor1 and self.valor2) == 0:
            return None
        else:
            return log(self.soma(), _base)

    def logaritmo2(self):
        if self.valor1 == 0:
            return log2(self.valor2)
        elif self.valor2 == 0:
            return log2(self.valor1)
        elif (self.valor1 and self.valor2) == 0:
            return None
        else:
            return log2(self.soma())

    def logaritmo10(self):
        if self.valor1 == 0:
            return log10(self.valor2)
        elif self.valor2 == 0:
            return log10(self.valor1)
        elif (self.valor1 and self.valor2) == 0:
            return None
        else:
            return log10(self.soma())

    def logaritmo_nat(self):
        if self.valor1 == 0:
            return log1p(self.valor2)
        elif self.valor2 == 0:
            return log1p(self.valor1)
        elif (self.valor1 and self.valor2) == 0:
            return None
        else:
            return log1p(self.soma())

    def seno(self):
        if self.valor1 == 0:
            return sin(self.valor2)
        elif self.valor2 == 0:
            return sin(self.valor1)
        elif (self.valor1 and self.valor2) == 0:
            return None
        else:
            return sin(self.soma())

    def coseno(self):
        if self.valor1 == 0:
            return cos(self.valor2)
        elif self.valor2 == 0:
            return cos(self.valor1)
        elif (self.valor1 and self.valor2) == 0:
            return None
        else:
            return cos(self.soma())

    def tangente(self):
        if self.valor1 == 0:
            return tan(self.valor2)
        elif self.valor2 == 0:
            return tan(self.valor1)
        elif (self.valor1 and self.valor2) == 0:
            return None
        else:
            return tan(self.soma())

    def arc_tangente(self):
        if self.valor1 == 0:
            return atan(self.valor2)
        elif self.valor2 == 0:
            return atan(self.valor1)
        elif (self.valor1 and self.valor2) == 0:
            return None
        else:
            return atan(self.soma())
