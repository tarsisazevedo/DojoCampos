from fatoresprimos import Numero
import unittest


class FatoresPrimos(unittest.TestCase):
    def test_fatores_de_1(self):
        fatores = Numero(1).fatores_primos
        self.assertEquals([], fatores)

    def test_fatores_de_2(self):
        fatores = Numero(2).fatores_primos
        self.assertEquals([2], fatores)

    def test_fatores_de_6(self):
        fatores = Numero(6).fatores_primos
        self.assertEquals([2,3],fatores)

    def test_fatores_de_10(self):
        fatores = Numero(10).fatores_primos
        self.assertEquals([2,5], fatores)

    def test_fatores_de_20(self):
        fatores = Numero(20).fatores_primos
        self.assertEquals([2,2,5], fatores)

    def test_fatores_de_100(self):
        fatores = Numero(100).fatores_primos
        self.assertEquals([2,2,5,5], fatores)

    def test_fatores_de_3(self):
        fatores = Numero(3).fatores_primos
        self.assertEquals([3], fatores)

    def test_fatores_de_27(self):
        fatores = Numero(27).fatores_primos
        self.assertEquals([3,3,3], fatores)

    def test_fatores_de_333(self):
        fatores = Numero(333).fatores_primos
        self.assertEquals([3,3,37], fatores)

    def test_fatores_de_333_duas_vezes(self):
        trezentos_e_trinta_e_tres = Numero(333)
        self.assertEquals([3,3,37], trezentos_e_trinta_e_tres.fatores_primos)
        self.assertEquals([3,3,37], trezentos_e_trinta_e_tres.fatores_primos)


if __name__ == '__main__':
    unittest.main()

