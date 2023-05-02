class HashNode:

    def __init__(self, key="", data=None):
        self.key = key
        self.data = data  # kan vara bara en sträng ex eller ett objekt
        self.next = None


class Hashtable:

    def __init__(self, size):
        self.size = size
        self.newtable = [None] * 2 * size  # la till 50 % luft

    def store(self, key, data):  # här skall krockhanteringen läggas till
        hashnyckel = self.hashfunction(key)

        if self.newtable[hashnyckel] == None:
            self.newtable[hashnyckel] = HashNode(key, data)
        elif self.newtable[hashnyckel].key == key:  # nod med samma nyckel men olika data, vill byta ut data
            self.newtable[hashnyckel].data = data
        else:

            current = self.newtable[hashnyckel]
            while current.next is not None:
                if current.next.key == key:
                    current.next.data = data
                    return
                current = current.next
            current.next = HashNode(key, data)

    def search(self, key):

        hashnyckel = self.hashfunction(key)
        if self.newtable[hashnyckel] is None:
            raise KeyError
        elif self.newtable[hashnyckel].key == key:
            return self.newtable[hashnyckel].data
        else:
            current = self.newtable[hashnyckel]
            while current.next is not None:
                if current.next.key == key:
                    return current.next.data
                current = current.next
            raise KeyError

    def hashfunction(self, key):

        objekt = list(key)
        x = 0
        for bokstav in objekt:
            x += ord(bokstav) ** 2
        return x % self.size
