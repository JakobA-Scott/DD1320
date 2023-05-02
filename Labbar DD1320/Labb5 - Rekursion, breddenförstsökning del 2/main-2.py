from bintreeFile import *
from linkedQFile import *

svenska = Bintree()
gamla = Bintree()
with open("word3.txt", "r", encoding="utf-8") as svenskafil:  # nästintill kopierad från förra labben
    startord = input("Ange startord: ")
    lista = list(startord)
    slutord = input("Ange slut ord: ")
    for rad in svenskafil:
        ordet = rad.strip()
        if ordet in svenska:
            pass
        else:
            svenska.put(ordet)

alfabet = list("abcdefghijklmnopqrstuvxyzåäö")
startnod = ParentNode(startord, None)

def makechildren(nod, q):
    if nod.word == slutord:
        writechain(nod)
        return True
    else:
        pass

    for char in range(3):  # varje ord är 3 bokatäver
        temp = list(nod.word)  # temporär lista
        for bokstav in alfabet:
            temp[char] = bokstav  # ändrar bokstaven på index [char] till bokstav i alfabetet
            new = "".join(temp)  # .join slår ihop alla bokstäver till ett ord
            if new in svenska:  # om det nya barnet som ifall sur nu är aur finns gör detta nedan
                if new in gamla:  # om barnet redan finns som en föräldrer någonstans vill vi inte lägga till det igen
                    pass
                elif new != startord and new != slutord:
                    ny = ParentNode(new, nod)
                    q.enqueue(ny)  # lägg till i kön och i dumbarnlistan q.enqueue(ParentNOde)
                    gamla.put(ny.word)
                elif new == slutord:  # om vi hittat ordet gör samma sak som ovan
                    ny = ParentNode(new, nod)
                    q.enqueue(ny)
                    gamla.put(ny.word)
                else:
                    break
            else:
                pass

def writechain(startnod):
    if startnod.parent is None:
        print(startnod.word)
    else:
        writechain(startnod.parent)
        print(startnod.word)



def main():
    q = LinkedQ()
    q.enqueue(startnod)
    while not q.isEmpty():
        nod = q.dequeue()
        if makechildren(nod, q) is True:  # om vi nått slutordet returnera True
            print("Det finns en väg")
            break
    if q.isEmpty():  # om ordet inte finns i svenska eller
        print("Det finns inte en väg")


main()