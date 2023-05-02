from bintreeFile import *
svenska = Bintree()  # samma bintreeFile som tidigare labb
#gamla = Bintree()
with open("word3.txt", "r", encoding = "utf-8") as svenskafil:
    startord = input("ange startord: ")
    lista  = list(startord)
    slutord = input("ange slutord: ")
    for rad in svenskafil:
        ordet = rad.strip()
        if ordet in svenska:
            pass
        else:
            svenska.put(ordet)

alfabet = list("abcdefghijklmnopqrstuvxyzåäö")


def makechildren():
    barn = []
    dumbarn = []

    for char in range(3):
        temp = lista
        for bokstav in alfabet:
            temp[char] = bokstav
            new = "".join(temp)  # .join slår ihop alla bokstäver till ett ord
            if new in svenska:
                if new in dumbarn:
                    pass
                elif new != startord and new != slutord:
                    barn.append(new)
                else:
                    break
            else:
                pass
    return barn

print(makechildren())








