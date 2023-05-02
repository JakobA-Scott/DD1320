from bintreeFile import *
svenska = Bintree()
engelska = Bintree()
with open("word3", "r", encoding = "utf-8") as svenskfil, open("engelska", "r") as data:
    for rad in svenskfil:
        ordet = rad.strip()                # Ett trebokstavsord per rad
        if ordet in svenska:
            pass
        else:
            svenska.put(ordet)  # in i sökträdet

    for meningar in data:
        rader = meningar.split()
        for ord in rader:
            allaord = ord
            if allaord in engelska:
                pass
            else:
                if allaord in svenska:
                    engelska.put(allaord)
                    print(allaord, end = " ")
                else:
                    pass












