class DictHash:
    def __init__(self):
        self._dict = {}

    def store (self, nyckel, data):
        self._dict[nyckel] = data

    def search (self, nyckel):
        return self._dict.get(nyckel)

    def __getitem__(self, nyckel): #anropar search metoden
        return self.search(nyckel)

    def __contains__(self, nyckel): #returnerar True om nyckeln finns, annars false
        return nyckel in self._dict[nyckel]