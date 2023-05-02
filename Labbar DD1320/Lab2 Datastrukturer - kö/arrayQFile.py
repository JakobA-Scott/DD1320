from array import array


class ArrayQ(object):

    def __init__(self):
        self._queue = array('b')   # inleds med understreck för att göra dem privata. Skapar en array

    def enqueue(self, x):  # stoppar in x SIST i kön
        self._queue.append(x)

    def dequeue(self):  # tar bort sista elementet ur kön
        return self._queue.pop(0)

    def isEmpty(self): #om kön är tom retunera True
        if len(self._queue) == 0:
            return True
        else:
            return False

    def Size(self):
        antal = self._queue
        x = len(antal)
        return x














