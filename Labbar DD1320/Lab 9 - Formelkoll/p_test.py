import unittest
from blubb import *

class LearnTest(unittest.TestCase):

    """TESTAR KORREKT SYNTAX"""
    def test_korrekt(self):
        formel = "Na"
        q = skapakö(formel)
        resultat = kolla_molekyl_formel(q)
        self.assertEqual(resultat, "Formeln är syntaktiskt korrekt ")

    def test_korrekt2(self):
        formel = "H2O"
        q = skapakö(formel)
        resultat = kolla_molekyl_formel(q)
        self.assertEqual(resultat, "Formeln är syntaktiskt korrekt ")

    def test_korrekt3(self):
        formel = "Si(C3(COOH)2)4(H2O)7"
        q = skapakö(formel)
        resultat = kolla_molekyl_formel(q)
        self.assertEqual(resultat, "Formeln är syntaktiskt korrekt ")


    def test_korrekt4(self):
        formel = "Na332"
        q = skapakö(formel)
        resultat = kolla_molekyl_formel(q)
        self.assertEqual(resultat, "Formeln är syntaktiskt korrekt ")

    def test_inkorrekt(self):
        formel = "C(Xx4)5"
        q = skapakö(formel)
        resultat = kolla_molekyl_formel(q)
        self.assertEqual(resultat, "Okänd atom vid radslutet 4)5")

    def test_inkorrekt1(self):
        formel = "C(OH4)C"
        q = skapakö(formel)
        resultat = kolla_molekyl_formel(q)
        self.assertEqual(resultat, "Saknad siffra vid radslutet C")

    def test_inkorrekt2(self):
        formel = "C(OH4C"
        q = skapakö(formel)
        resultat = kolla_molekyl_formel(q)
        self.assertEqual(resultat, "Saknad högerparentes vid radslutet ")

    def test_inkorrekt3(self):
        formel = "H2O)Fe"
        q = skapakö(formel)
        resultat = kolla_molekyl_formel(q)
        self.assertEqual(resultat, "Felaktig gruppstart vid radslutet )Fe")

    def test_inkorrekt4(self):
        formel = "H0"
        q = skapakö(formel)
        resultat = kolla_molekyl_formel(q)
        self.assertEqual(resultat, "För litet tal vid radslutet ")
    #
    def test_inkorrekt5(self):
        formel = "H1C"
        q = skapakö(formel)
        resultat = kolla_molekyl_formel(q)
        self.assertEqual(resultat, "För litet tal vid radslutet C")

    def test_inkorrekt6(self):
        formel = "H02C"
        q = skapakö(formel)
        resultat = kolla_molekyl_formel(q)
        self.assertEqual(resultat, "För litet tal vid radslutet 2C")

    def test_inkorrekt7(self):
        formel = "Nacl"
        q = skapakö(formel)
        resultat = kolla_molekyl_formel(q)
        self.assertEqual(resultat, "Saknad stor bokstav vid radslutet cl")

    def test_inkorrekt8(self):
        formel = "a"
        q = skapakö(formel)
        resultat = kolla_molekyl_formel(q)
        self.assertEqual(resultat, "Saknad stor bokstav vid radslutet a")

    def test_inkorrekt9(self):
        formel = "(Cl)2)3"
        q = skapakö(formel)
        resultat = kolla_molekyl_formel(q)
        self.assertEqual(resultat, "Felaktig gruppstart vid radslutet )3")
    #
    def test_inkorrekt10(self):
        formel = ")"
        q = skapakö(formel)
        resultat = kolla_molekyl_formel(q)
        self.assertEqual(resultat, "Felaktig gruppstart vid radslutet )")

    def test_inkorrekt11(self):
        formel = "2"
        q = skapakö(formel)
        resultat = kolla_molekyl_formel(q)
        self.assertEqual(resultat, "Felaktig gruppstart vid radslutet 2")







if __name__ == '__main__':
    unittest.main()