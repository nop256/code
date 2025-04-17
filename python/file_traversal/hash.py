#implemented as a hash table
#make resizeable
class bag:
    def __init__(self, expectedSize=101):
        size = expectedSize * 2 + 1
        while not self.isprime(size): 
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

    def exists(self, elt):
        key = hash(elt)
        index = key % len(self.table)
        start = index
        while True:
            if self.table[index] is None: return False
            if self.table[index] and self.table[index] == elt: return True      
            index+=1
            if index >= len(self.table): index=0
            if index == start:
                return False
            
    def insert(self, elt):
        if self.exists(elt): return False
        if self.count > len(self.table) * 0.66:
            old = self.table
            newsize = len(self.table) * 2 + 1
            while not self.isprime(newsize):
                newsize += 2
            self.table = [None] * newsize
            self.count = 0
            for entry in old:
                if entry:
                    self.insert(entry)  #reinsert each from old
        key = hash(elt)
        index = key % len(self.table)
        while True:
            if self.table[index] is None or not self.table[index]:
                self.table[index] = elt
                self.count += 1
                return True
            index = (index+1) % len(self.table)
            
    def delete(self, elt):
        key = hash(elt)
        index = key % len(self.table)
        start = index
        while True:
            if self.table[index] is None: return False
            if self.table[index] and self.table[index] == elt:
                self.table[index] = False
                self.count -= 1
                return True
            index = (index + 1) % len(self.table)
            if index == start:
                return False
            
    def retrieve(self, elt):
        key = hash(elt)
        index = key % len(self.table)
        start = index
        while True:
            slot = self.table[index]
            if slot is None:
                return None
            if slot and slot == elt:
                return slot
            index = (index + 1) % len(self.table)
            if index == start:
                return None
    
    def size(self):
        return self.count
    
    def __iter__(self):
        for slot in self.table:
            if slot: yield slot
                
