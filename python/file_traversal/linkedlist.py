class Node:
    def __init__(self,item,nxt=None):
        self.item = item
        self.nxt = nxt        

class Bag:
    """A container class that stores unique items in an unordered manner."""

    def __init__(self):
        self.first=None

    def insert(self,item):
        if self.exists(item):
            return False
        n = Node(item,self.first)
        self.first=n
        return True
        """
        if self.exists(item):
            return False
        else:
            self.bag.append(item)
            return True
        """
        
    def retrieve(self,item):
        current = self.first
        while current:
            if current.item == item: return current.item
            current = current.nxt
        return None
        """
        for obj in self.bag:
            if item == obj:
                return obj
        return None
        """
    
    def delete(self,item):
        if not self.exists(item): return False
        if self.first.item == item: 
            self.first = self.first.nxt
            return True
        current = self.first
        while current.nxt.item != item: current = current.nxt
        current.nxt = current.nxt.nxt
        return True
        """
        for obj in self.bag:
            if obj == item:
                self.bag.remove(obj)
                return True
        return False
        """
    
    def __iter__(self):
        current = self.first
        while current:
            yield current.item
            current = current.nxt
        """
        for item in self.bag:
            yield item
        """
        

    def exists(self,item):
        current = self.first
        while current:
            if current.item == item:
                return True
            current = current.nxt
        return False
        """
        for obj in self.bag:
            if obj == item:
                return True
        return False
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
