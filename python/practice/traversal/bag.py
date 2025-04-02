from student import Student


class bag:
    def __init__(self):
        self.bag = []

    def insert(self, elt):
        if self.exists(elt): return False
        self.bag.append(elt)
        return True

    def exists(self, elt):
        for obj in self.bag:
            if obj == elt: return True
            return False

    def size(self):
        return len(self.bag)

    def print(self):
        return self.bag

