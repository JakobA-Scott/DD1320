from bintreeFile import *
from linkedQFile import *

svenska = Bintree()
#gamla = Bintree()
with open("word3.txt", "r", encoding="utf-8") as svenskafil:  # nästintill kopierad från förra labben
    startord = input("ange startord: ")
    lista = list(startord)
    slutord = input("ange slut ord: ")
    for rad in svenskafil:
        ordet = rad.strip()
        if ordet in svenska:
            pass
        else:
            svenska.put(ordet)

alfabet = list("abcdefghijklmnopqrstuvxyzåäö")
dumbarn = []  # tom lista att fylla alla barnen i så vi slipper dumbarn


def makechildren(nod, q):
    if nod == slutord: #kolla main för full förståelse
        return True
    else:
        pass

    for char in range(3):  # varje ord är 3 bokatäver
        temp = list(nod)  # temporär lista
        for bokstav in alfabet:
            temp[char] = bokstav  # ändrar bokstaven på index [char] till bokstav i alfabetet
            new = "".join(temp)  # .join slår ihop alla bokstäver till ett ord
            if new in svenska:  # om det nya barnet som ifall sur nu är aur finns gör detta nedan
                if new in dumbarn:  # om barnet redan finns som en föräldrer någonstans vill vi inte lägga till det igen
                    pass
                elif new != startord and new != slutord:
                    q.enqueue(new)  # lägg till i kön och i dumbarnlistan
                    dumbarn.append(new)
                elif new == slutord:  # om vi hittat ordet gör samma sak som ovan
                    q.enqueue(new)
                    dumbarn.append(new)
                else:
                    break
            else:
                pass


def main():
    q = LinkedQ()
    q.enqueue(startord)
    while not q.isEmpty():
        nod = q.dequeue()
        if makechildren(nod, q) is True:  # om vi nått slutordet returnera True
            print("det finns en väg")
            break
    if q.isEmpty():  # om ordet inte finns i svenska eller
        print("Det finns inte en väg")


main()