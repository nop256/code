

class Node:
    def __init__(self,elt,nxt=None):
        self.elt=elt
        self.nxt=nxt

class Bag:
    def __init__(self):
        self.first=None

    def insert(self, elt):
        if self.exists(elt):
            return False
        self.first = Node(elt, self.first)
        return True

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
        return True

    def retrieve(self, elt):
        current = self.first
        while current:
            if current.elt == elt:
                return current.elt
            current = current.nxt
        return None

    def __iter(self):
        current = self.first
        while current:
            yield current.elt
            current = current.nxt

    def exists(self, elt):
        current = self.first
        while current:
            if current.elt == elt:
                return True
            current = current.nxt
        return False

    def size(self):
        current = self.first
        size = 0
        while current:
            size += 1
            current = current.nxt
        return size
