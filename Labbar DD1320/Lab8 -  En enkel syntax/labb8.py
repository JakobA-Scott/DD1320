from linkedQFile import *

class Syntaxfel(Exception):
    pass

def kolla_molekyl_formel(q):
    try:
        molekyl(q)
        return "Formeln är syntaktiskt korrekt "
    except Syntaxfel as felet:
        return str(felet)

def skapakö(molekyl_formel):
    q = LinkedQ()
    for x in molekyl_formel:
        q.put(x)
    q.put("§")
    return q

#Källa: Föreläsning 12 VT2021
def printQueue(q):
    word1 = ""
    while q.peek() is not "§" and not q.isEmpty():
        word = q.dequeue()
        word1 = word1 + word
    return word1

def molekyl(q):
    atom(q)
    symbol = q.peek()
    if symbol.isnumeric():
        num(q)
        return "Formeln är syntaktiskt korrekt "
    elif symbol.isalpha():
        raise Syntaxfel("För litet tal vid radslutet " + printQueue(q))
    else:
        return

def atom(q):
    while q.peek() is not "§":
        letter1(q)
        temp = q.peek()
        if temp.isalpha():
            letter2(q)
        return


def letter1(q):
    bokstav = q.peek()
    x = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if bokstav in x:
        q.dequeue()
        return
    else:
        raise Syntaxfel("Saknad stor bokstav vid radslutet " + printQueue(q))


def letter2(q):
    bokstav = q.peek()
    x = "abcdefghijklmnopqrstuvwxyz"
    if bokstav in x:
        q.dequeue()
        return
    else:
        raise Syntaxfel("Saknad stor bokstav vid radslutet " + printQueue(q))

def num(q):
    num = q.peek()
    if int(num) == 0:
        q.dequeue()
        raise Syntaxfel("För litet tal vid radslutet " + printQueue(q))
    elif num.isnumeric() and num != "§":
        num = q.dequeue()
        while q.peek().isnumeric():
            num = num + q.dequeue()
        num = int(num)
        if num >= 2:
            num = str(num)
            return num
        else:
            raise Syntaxfel("För litet tal vid radslutet " +  printQueue(q))
    else:
        raise Syntaxfel("För litet tal vid radslutet " + printQueue(q))

def main():
    formel = input().strip()
    while formel != "#":
            q = skapakö(formel)
            output = kolla_molekyl_formel(q)
            print(output)
            formel = input().strip()










