class node:
    def __init__(self, elt):
        self.elt = elt
        self.l = None
        self.r = None

class bag:
    def __init__(self):
        self.root = None

    def insert(self, elt):
        if self.exists(elt):
            return False
        self.root = self.insertR(elt, self.root)
        return True

    def insertR(self, elt, current):
        pass

    def exists(self, elt):
        return self.existsR(elt, self.root)

    def existsR(self, elt, current):
        if current is None: return False
        elif current == current.elt: return True
        elif current < current.elt: return self.existsR(elt, current.l)
        elif current > current.elt: return self.existsR(elt, current.r)

    def retrieve(self, elt):
        return self.retrieveR(elt, self.root)

    def retrieveR(self, elt, current):
        if not self.exists(elt): return False
        if current is None: return None
        elif current == current.elt: return current.elt
        elif current < current.elt: return self.retrieveR(elt, current.l)
        elif current > current.elt: return self.retrieveR(elt, current.r)

    def size(self):
        return self.sizeR(self.root)

    def sizeR(self, current):
        if current is None: return 0
        return 1 + self.sizeR(current.l) + self.sizeR(current.r)

    def __iter__(self):
        yield from self.iterR(self.root)

    def iterR(self, current):
        if current is not None:
            yield from self.iterR(current.l)
            yield current.elt
            yield from self.iterR(current.r)
