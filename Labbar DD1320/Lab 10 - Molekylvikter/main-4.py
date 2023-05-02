from linkedQFile import *
from molgrafik import *
from hashtest import *


class Ruta:
    def __init__(self, atom="()", num=1):
        self.atom = atom
        self.num = num
        self.next = None
        self.down = None


class Syntaxfel(Exception):
    pass


atomer = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K',
          'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb',
          'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs',
          'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta',
          'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa',
          'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt',
          'Ds', 'Rg', 'Cn', 'Fl', 'Lv']


def kolla_molekyl_formel(q): #kollad
    try:
        mol = molekyl(q)
        if not q.isEmpty():
            raise Syntaxfel("Felaktig gruppstart vid radslutet " + printQueue(q))
        else:
            return mol
    except Syntaxfel as felet:
        return str(felet)



def grupp(q):  # <group> ::= <atom> |<atom><num> | (<mol>) <num>  #kollat
    rutan = Ruta()
    if not q.isEmpty() and q.peek() == "(":
        q.dequeue()
        rutan.down = molekyl(q)  # =?
        if not q.isEmpty() and q.peek() == ")":
            q.dequeue()
        else:
            raise Syntaxfel("Saknad högerparentes vid radslutet " + printQueue(q))
        if q.isEmpty() or q.peek().isalpha():
            raise Syntaxfel("Saknad siffra vid radslutet " + printQueue(q))
        elif q.peek().isnumeric():
            rutan.num = int(num(q))
            return rutan
    elif not q.isEmpty() and q.peek() == ")":
        raise Syntaxfel("Felaktig gruppstart vid radslutet " + printQueue(q))
    rutan.atom = kolla_atom(q)
    if q.isEmpty():
        return rutan
    if not q.isEmpty() and q.peek().isnumeric():
        rutan.num = int(num(q))
    return rutan


def molekyl(q):  # <mol>::= <group> | <group><mol> #villkollw
    while not q.isEmpty():
        mol = grupp(q)
        if not q.isEmpty() and q.peek() != ")":
            mol.next = molekyl(q)
            return mol
        else:
            return mol




def kolla_atom(q):
    first = letter1(q)
    if not q.isEmpty():
        second = letter2(q)
        atomen = first + second
        if atomen not in atomer:
            raise Syntaxfel("Okänd atom vid radslutet " + printQueue(q))
        return atomen
    elif first not in atomer:
        raise Syntaxfel("Okänd atom vid radslutet " + printQueue(q))
    return


def letter1(q):
    bokstav = q.peek()
    x = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # borde gjort isupper() ist
    if bokstav in x:
        first = q.dequeue()
        return first
    elif bokstav.isnumeric():
        raise Syntaxfel("Felaktig gruppstart vid radslutet " + printQueue(q))
    else:
        raise Syntaxfel("Saknad stor bokstav vid radslutet " + printQueue(q))


def letter2(q):
    bokstav = q.peek()
    x = "abcdefghijklmnopqrstuvwxyz"
    if bokstav in x:
        return q.dequeue()
    else:
        return ""


def num(q):
    num = q.peek()
    if int(num) == 0:
        q.dequeue()
        raise Syntaxfel("För litet tal vid radslutet " + printQueue(q))
    elif num.isnumeric() and num != "§":
        num = q.dequeue()
        while not q.isEmpty() and q.peek().isnumeric():
            num = num + q.dequeue()
        num = int(num)
        if num >= 2:
            num = str(num)
            return num
        else:
            raise Syntaxfel("För litet tal vid radslutet " + printQueue(q))
    else:
        raise Syntaxfel("För litet tal vid radslutet " + printQueue(q))


def skapakö(molekyl_formel):
    q = LinkedQ()
    for x in molekyl_formel:
        q.put(x)
    return q


# Källa: Föreläsning 12 VT2021
def printQueue(q):
    word1 = ""
    while not q.isEmpty():
        word = q.dequeue()
        word1 = word1 + word
    return word1


def weight(output):
    viktlista = skapaAtomlista()
    hashlista = lagraHashtabell(viktlista)
    if output is not None:
        if output.down is not None:
            vikt = (output.num * weight(output.down))
        else:
            vikt = output.num * hashlista.search(output.atom).vikt
        return vikt + weight(output.next)
    return 0


def main():
    formel = input()
    while formel != "#":
        mg = Molgrafik()
        q = skapakö(formel)
        output = kolla_molekyl_formel(q)
        vikt = weight(output)
        print("Molekylens vikt är:", vikt)
        mg.show(output)
        formel = input()

main()