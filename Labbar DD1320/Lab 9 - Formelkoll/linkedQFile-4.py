class Node:
    def __init__(self, data, nxt=None):
        self.data = data #två attribut, data och en nextpekare
        self.next = nxt

class LinkedQ:

    def __init__(self):
        self.head = None #första kortet i kön
        self._tail = None #sista kortet i kön

    def put(self, x):
        """"" Stoppar in x sist i kön """

        ny = Node(x)
        if self.head == None:
            self.head = ny
            self._tail = ny

        else:
            self._tail.next = ny
            self._tail = ny

    def peek(self):
        return self.head.data

    def dequeue(self):
        """plockar ut och retunerar det som står först i kön"""

        if self.head == None:
            return None
        else:
            x = self.head.data
            self.head = self.head.next
            return x

    def isEmpty(self):
        """Kollar om det finns en head, om det inte finns betyder det att kön är tom"""
        if self.head == None:
            return True
        else:
            return False

    def Size(self):
        antal = 0
        p = self.head
        while not p == None:
            antal += 1
            p = p.next
        return antal
