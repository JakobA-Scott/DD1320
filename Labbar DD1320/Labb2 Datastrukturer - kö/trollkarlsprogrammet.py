from arrayQFile import *
from linkedQFile import *


def main():
    #queue = ArrayQ()
    queue = LinkedQ()
    data = input("Skriv in korten 1-13 i valfri ordning med mellanrum mellan varje kort\n")
    """kan vi ändra detta sen?"""
    temp = data.split() #stor lista med strings

    for i in temp:
        queue.enqueue(int(i))

    print("Antalet kort i kortleken är:", queue.Size(), "\n", "\nSimsalabim")

    while not queue.isEmpty():  # första kortet läggs längst bak, andra kortet tas ur leken, repeat
            head = queue.dequeue()
            queue.enqueue(head)
            visade_kort = queue.dequeue()
            print(visade_kort)

main()




