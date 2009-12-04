#encoding: utf-8
"""
>>> frutas = {'banana': 1, 'maça': 2, 'laranja': 5, 'limao':0.75}
>>> hortiFruti = HortiFruti(frutas)
>>> hortiFruti.colocar_dinheiro(1)
>>> hortiFruti.escolher_fruta('banana')
'banana'
>>> hortiFruti.escolher_fruta('maça')
Traceback (most recent call last):
...
DinheiroInsuficiente: Sem dinheiro suficiente

>>> hortiFruti.colocar_dinheiro(3)
Traceback (most recent call last):
...
DinheiroInvalido: Você só pode inserir até 1 dinheiro

>>> hortiFruti.colocar_dinheiro(1)
>>> hortiFruti.colocar_dinheiro(1)
>>> hortiFruti.colocar_dinheiro(1)
>>> print hortiFruti.escolher_fruta('maça')
maça
>>> print hortiFruti.escolher_fruta('banana')
banana
>>> print hortiFruti.escolher_fruta('banana')
Traceback (most recent call last):
...
DinheiroInsuficiente: Sem dinheiro suficiente

>>> hortiFruti.colocar_dinheiro(0.25)
>>> hortiFruti.colocar_dinheiro(0.50)
>>> print hortiFruti.escolher_fruta("limao")
limao
>>> hortiFruti.colocar_dinheiro(1)
>>> hortiFruti.colocar_dinheiro(0.50)
>>> print hortiFruti.escolher_fruta("limao")
limao
>>> print hortiFruti.escolher_fruta("limao")
limao
>>> hortiFruti.colocar_dinheiro(1)
>>> hortiFruti.devolver_dinheiro()
1.0

>>> hortiFruti.colocar_dinheiro(1)
>>> hortiFruti.devolver_dinheiro()
1.0

>>> hortiFruti.colocar_dinheiro(0.25)
>>> hortiFruti.devolver_dinheiro()
0.25

>>> hortiFruti.colocar_dinheiro(1)
>>> hortiFruti.escolher_fruta('limao')
'limao'
>>> hortiFruti.devolver_dinheiro()
0.25
"""
import doctest

class DinheiroInvalido(Exception):
    pass

class DinheiroInsuficiente(Exception):
    pass

class HortiFruti:
    def __init__(self, frutas):
        self.frutas = frutas
        self.dinheiro_na_maquina = 0.0

    def colocar_dinheiro(self, dinheiro):
        if dinheiro not in (0.25, 0.50, 1.0):
             raise DinheiroInvalido('Você só pode inserir até 1 dinheiro')
        self.dinheiro_na_maquina += dinheiro

    def escolher_fruta(self, fruta):
        valor = self.frutas.get(fruta)
        if valor <= self.dinheiro_na_maquina:
            self.dinheiro_na_maquina -= valor
            return fruta
        raise DinheiroInsuficiente('Sem dinheiro suficiente')

    def devolver_dinheiro(self):
        dinheiro = self.dinheiro_na_maquina
        self.dinheiro_na_maquina = 0.0
        return dinheiro

doctest.testmod(optionflags = doctest.ELLIPSIS)

