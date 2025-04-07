class Node:
    def __init__(self,elt,nxt=None):
        self.elt = elt
        self.nxt = nxt        

class Bag:
    """A container class that stores unique elts in an unordered manner."""

    def __init__(self):
        self.first=None

    def insert(self,elt):
        if self.exists(elt):
            return False
        n = Node(elt,self.first)
        self.first=n
        return True
        """
        if self.exists(elt):
            return False
        else:
            self.bag.append(elt)
            return True
        """

    def exists(self,elt):
        current = self.first
        while current:
            if current.elt == elt:
                return True
            current = current.nxt
        return False
        """
        for obj in self.bag:
            if obj == elt:
                return True
        return False
        """

     def delete(self,elt):
        if not self.exists(elt): return False
        if self.first.elt == elt: 
            self.first = self.first.nxt
            return True
        current = self.first
        while current.nxt.elt != elt: current = current.nxt
        current.nxt = current.nxt.nxt
        return True
        """
        for obj in self.bag:
            if obj == elt:
                self.bag.remove(obj)
                return True
        return False
        """
        
    def retrieve(self,elt):
        current = self.first
        while current:
            if current.elt == elt: return current.item
            current = current.nxt
        return None
        """
        for obj in self.bag:
            if elt == obj:
                return obj
        return None
        """
    
    def size(self):
        size = 0
        current = self.first
        while current:
            size += 1
            current = current.nxt
        return size
        """
        return len(self.bag)
        """
    
    def __iter__(self):
        current = self.first
        while current:
            yield current.elt
            current = current.nxt
        """
        for elt in self.bag:
            yield elt
        """


def main():
    bag = Bag()
    bag.insert('A')
    bag.insert('B')
    bag.insert('C')
    bag.insert('D')
    bag.insert('E')
    bag.insert('F')
    for student in bag: print(student)
    
    print("C" in bag)
    print("Z" in bag)
    print(bag.size())
    

#main()
