class node:
    def __init__(self, elt, nxt=None):
        self.elt = elt
        self.nxt = nxt

class bag:
    def __init__(self):
        self.first = None
    
    def insert(self, elt):
        if self.exists(elt):
            return False
        self.first = node(elt, self.first)
        return True

    def exists(self, elt):
        current = self.first
        while current:
            if current.elt == elt:
                return True
            current = current.nxt
        return False

    def delete(self, elt):
        if not self.exists(elt):
            return False
        if self.first.elt == elt:
            self.first = self.first.nxt
            return True
        current = self.first
        while current.nxt.elt != elt:
            current = current.nxt
        current.nxt = current.nxt.nxt
        #current = current.nxt
        return True

    def retrieve(self, elt):
        current = self.first
        while current:
            if current.elt == elt:
                return current.elt
            current = current.nxt
        return None

    def size(self):
        size = 0
        current = self.first
        while current:
            size += 1
            current = current.nxt
        return size

    def __iter__(self):
        current = self.first
        while current:
            yield current
            current = current.nxt

