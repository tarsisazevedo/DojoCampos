class Numero(object):
    def __init__(self, numero):
        self._numero = numero

    @property
    def fatores_primos(self):
        numero = self._numero
        divisor = 2
        fatores = []
        while numero >= divisor:
            while numero % divisor == 0:
                numero /= divisor
                fatores.append(divisor)
            divisor += 1
        return fatores
4

