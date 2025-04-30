class node:
    def __init__(self, elt):
        self.elt = elt
        self.l = None
        self.r = None

class bag:
    def __init__(self):
        self.root = None

    def exists(self, elt):
        return self.existsR(elt, self.root)
    
    def existsR(self, elt, current):
        if current is None: return False
        elif elt == current.elt: return True
        elif elt < current.elt: return self.existsR(elt, current.l)
        elif elt > current.elt: return self.existsR(elt, current.r)

    def insert(self, elt):
        if self.exists(elt): return False
        self.root = self.insertR(elt, self.root)
        return True

    def insertR(self, elt, current):
        if current is None: current = node(elt)
        elif elt < current.elt: current.l = self.insertR(elt, current.l)
        elif elt > current.elt: current.r = self.insertR(elt, current.r)
        return current

    def delete(self, elt):
        if not self.exists(elt): return False
        self.root = self.deleteR(elt, self.root)
        return True

    def deleteR(self, elt, current):
        if current is None: return None
        if elt < current.elt: current.l = self.deleteR(elt, current.l)
        elif elt > current.elt: current.r = self.deleteR(elt, current.r)
        else:
            if current.l is None and current.r is None: return None
            elif current.l is None: return current.r
            elif current.r is None: return current.l
            successor = current.r
            while successor.l is not None:
                successor = successor.l
            current.elt = successor.elt
            current.r = self.deleteR(successor.elt, current.r)
        return current

    def __iter__(self):
        yield from self.iterR(self.root)

    def iterR(self, current):
        if current is not None:
            yield from self.iterR(current.l)
            yield current.elt
            yield from self.iterR(current.r)

    def retrieve(self, elt):
        return self.retrieveR(elt, self.root)

    def retrieveR(self, elt, current):
        if not self.exists(elt): return False
        if current is None: return None
        if elt == current.elt: return current.elt
        elif elt < current.elt: return self.retrieveR(elt, current.l)
        else: return self.retrieveR(elt, current.r)

    def size(self):
        return self.sizeR(self.root)

    def sizeR(self, current):
        if current is None: return 0
        return 1 + self.sizeR(current.l) + self.sizeR(current.r)

