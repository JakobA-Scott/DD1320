import unittest
from labb8 import *

class LearnTest(unittest.TestCase):

    def test_func1(self):
        formel = "1"
        q = skapakö(formel)
        resultat = kolla_molekyl_formel(q)
        self.assertEqual(resultat, "Saknad stor bokstav vid radslutet " + formel)

    def test_func2(self):
        formel ="Cr02"
        q = skapakö(formel)
        resultat = kolla_molekyl_formel(q)
        self.assertEqual(resultat, "För litet tal vid radslutet 2" )

    def test_func3(self):
        formel ="Pga07"
        q = skapakö(formel)
        resultat = kolla_molekyl_formel(q)
        self.assertEqual(resultat, "För litet tal vid radslutet a07" )

    def test_func4(self):
        formel ="aa"
        q = skapakö(formel)
        resultat = kolla_molekyl_formel(q)
        self.assertEqual(resultat, "Saknad stor bokstav vid radslutet " + str(formel))

    def test_func5(self):
        formel ="Aa10"
        q = skapakö(formel)
        resultat = kolla_molekyl_formel(q)
        self.assertEqual(resultat, "Formeln är syntaktiskt korrekt ")



if __name__ == '__main__':
    unittest.main()