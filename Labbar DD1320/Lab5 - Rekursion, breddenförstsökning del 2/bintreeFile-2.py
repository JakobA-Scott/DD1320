class Bintree:
    def __init__(self):
        self.root = None

    def put(self,newvalue):
        # Sorterar in newvalue i trädet
        self.putta(self.root,newvalue)

    def __contains__(self,newvalue):
        # True om value finns i trädet, False annars
        return self.finns(self.root, newvalue)

    def write(self):
        # Skriver ut trädet i inorder
        self.skriv(self.root)
        print("\n")

    def putta(self, nod, newvalue):
        if self.root == None:
            self.root = Node(newvalue)
        else:
            if newvalue > nod.value:
                if nod.right == None:
                    nod.right = Node(newvalue)
                self.putta(nod.right, newvalue)
            elif newvalue < nod.value:
                if nod.left == None:
                    nod.left = Node(newvalue)
                self.putta(nod.left, newvalue)
            else:
                pass

    def skriv(self, nod):
        if nod is not None:
            self.skriv(nod.left)
            print(nod.value)
            self.skriv(nod.right)

    def finns(self, nod, newvalue):
        if nod == None:
            return False
        if nod.value == newvalue:
            return True
        elif newvalue > nod.value:
            return self.finns(nod.right, newvalue)
        elif newvalue < nod.value:
            return self.finns(nod.left, newvalue)
        else:
            return False


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class ParentNode:
    def __init__(self, word, parent = None):
        self.word = word
        self.parent = parent