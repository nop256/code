
"""
class student:
    def __hash__(self):
        self.ssn.replace(
"""
#implemented as a hash table
#resizeable?
class bag:
    def __init__(self, expectedSize=101):
        """make table a set size, when it gets 2/3's full make another one twice as big as what it was, remove expectedSize"""
        size = expectedSize * 2 + 1
        while not self.isprime(size): # take square root of it, try all numbers through the square root...
            size += 2
        self.table = [None] * size
        self.count = 0
        
    def isprime(self, n):
        if n < 2: return False
        if n == 2 or n == 3: return True
        if n % 2 == 0: return False
        for i in range(3, int(n**0.5)+1, 2):
            if n % i == 0: return False
        return True

    def exists(self, elt): # have to as elt to represent itself as an integer
        key = hash(elt)
        index = key % len(self.table)
        start = index
        while True:
            slot = self.table[index]
            if slot is None: return False
            if slot != "<deleted>" and slot == elt: return True      
            index+=1
            if index >= len(self.table): index=0
            if index == start:
                return False
            
    def insert(self, elt):
        slot = self.table[index]
        if self.exists(elt): return False
        if self.count > (2 * len(self.table)) // 3:
            old = self.table
            newsize = len(self.table) * 2 + 1
            while not self.isprime(newsize):
                newsize += 2
            self.table = [None] * newsize
            self.count = 0
            for entry in old:
                if entry is not None and entry != "<deleted>":
                    self.insert(entry)  #reinsert each from old
                    
        key = hash(elt)
        index = key % len(self.table)
        while True:
            if slot is None or slot == "<deleted>":
                slot = elt
                self.count += 1
                return True
            index = (index+1) % len(self.table)
            
    def delete(self, elt):
        key = hash(elt)
        index = key % len(self.table)
        start = index
        slot = self.table[index]
        while True:
            if slot is None: return False
            if slot != "<deleted>" and slot == elt:
                slot = "<deleted>"
                self.count -= 1
                return True
            index = (index + 1) % len(self.table)
            if index == start:
                return False
            
    def retrieve(self, elt):
        key = hash(elt)
        index = key % len(self.table)
        start = index
        slot = self.table[index]
        while True:
            if slot is None:
                return None
            if slot != "<deleted>" and slot == elt:
                return slot
            index = (index + 1) % len(self.table)
            if index == start:
                return None
    
    def size(self):
        return self.count
    
    def __iter__(self):
        for slot in self.table:
            if slot is not None and slot != "<deleted>":
                yield slot
                
