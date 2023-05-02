class Node:
    def __init__(self, data, nxt=None):
        self.data = data #två attribut, data och en nextpekare
        self.next = nxt

class LinkedQ:

    def __init__(self):
        self._head = None #första kortet i kön
        self._tail = None #sista kortet i kön

    def enqueue (self, x):
        """"" Stoppar in x sist i kön """

        ny = Node(x)
        if self._head == None:
            self._head = ny
            self._tail = ny

        else:
            self._tail.next = ny
            self._tail = ny

    def dequeue(self):
        """plockar ut och retunerar det som står först i kön"""

        if self._head == None:
            return None
        else:
            x = self._head.data
            self._head = self._head.next
            return x

    def isEmpty(self):
        """Kollar om det finns en head, om det inte finns betyder det att kön är tom"""
        if self._head == None:
            return True
        else:
            return False

    def Size(self):
        antal = 0
        p = self._head
        while not p == None:
            antal += 1
            p = p.next
        return antal