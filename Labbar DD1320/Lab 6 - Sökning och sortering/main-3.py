from songs import *
from timeit import *

#tre stycken sökningar: linjärsökning, binärsökning och hastabell

def kategoriskapare():
    with open("unique_tracks.txt", 'r') as file:
        data = file.readlines()
    lategenskaper = list()
    lategenskaper2 = dict()
    for latkategorier in data:
        temp = latkategorier.split("<SEP>")
        temp_latk = Songs(temp[0], temp[1], temp[2], temp[3])
        lategenskaper.append(temp_latk)
    return lategenskaper, lategenskaper2


def linjarsokning(lategenskaper, nyckel):
    for låt in lategenskaper:
        if låt.låttitel == nyckel:
            return True
    return False

def binsök(lategenskaper, nyckel):
    if len(lategenskaper) == 0:
        return False

    mitten = lategenskaper[len(lategenskaper)//2]
    mittenindex = len(lategenskaper)//2
    if mitten.låttitel == nyckel:
        return True
    elif mitten.låttitel < nyckel:
        binsök(lategenskaper[mittenindex:], nyckel)
    else:
        binsök(lategenskaper[:mittenindex], nyckel)

def hashsök(lategenskaper2, nyckel):
    for låt in lategenskaper2:
        if låt.låttitel == nyckel:
            return
    return False

def bubblesort(lategenskaper):
    n = len(lategenskaper)
    bytt = True
    i = 0
    while bytt:
        bytt = False # optimister, tror att just detta varv görs inga byten
        for j in range(n-1-i):
            if lategenskaper[j+1] < lategenskaper[j]: #jmf
                lategenskaper[j+1], lategenskaper[j] = lategenskaper[j], lategenskaper[j+1] #sw
                bytt = True
        i += 1


def mergesort(lategenskaper):
    if len(lategenskaper) > 1: #fler än ett element som behöver sorteras, det rekursiva basfallet.
        mitten = len(lategenskaper)//2 #beräknar vart mitten är
        vensterHalva = lategenskaper[:mitten] #skapar en kopia, extra minne
        hogerHalva = lategenskaper[mitten:] # skapar en kopia, extra minne

        mergesort(vensterHalva) #rekursivt sortering
        mergesort(hogerHalva)

        i, j, k = 0, 0, 0 #mergear

        while i < len(vensterHalva) and j < len(hogerHalva): #denna whileslinga mergear
            if vensterHalva[i] < hogerHalva[j]:
                lategenskaper[k] = vensterHalva[i]
                i = i + 1
            else:
                lategenskaper[k] = hogerHalva[j]
                j = j + 1
            k = k + 1

        while i < len(vensterHalva): #måste kolla om det finns element kvar i vä
            lategenskaper[k] = vensterHalva[i]
            i = i + 1
            k = k + 1

        while j < len(hogerHalva): #måste kolla om det finns element kvar i hö
            lategenskaper[k] = hogerHalva[j]
            j = j + 1
            k = k + 1


def main():
    lategenskaper,lategenskaper2 = kategoriskapare()
    nyckel = lategenskaper[len(lategenskaper)-1].låttitel
    t1 = timeit(stmt=lambda: linjarsokning(lategenskaper, nyckel), number=5)
    lategenskaper.sort()
    t = timeit(stmt=lambda: binsök(lategenskaper,nyckel), number=5)
    t2 = timeit(stmt=lambda: hashsök(lategenskaper2, nyckel), number=5)
    #mindrelista = lategenskaper[0:1000]
    # t3 = timeit(stmt=lambda: bubblesort(mindrelista), number=5)
    # t4 = timeit(stmt=lambda: mergesort(mindrelista), number=5)

    print("snitttiden för anropet av binärsökning tog", round(t,4), "sekunder.")
    print("snitttiden för anropet av linjärsökning tog", round(t1,4), "sekunder.")
    print("snitttiden för anropet av hashsökning tog", round(t2,10), "sekunder.")

    # print("snitttiden för anropet av bubbelsortering tog", round(t3, 4), "sekunder.")
    # print("snitttiden för anropet av mergesortering tog", round(t4, 4), "sekunder.")



main()


