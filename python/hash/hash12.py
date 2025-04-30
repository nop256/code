from isprime import isprime
class bag:
    def __init__(self,esize:int=30001):
        size=esize*2+1
        while not isprime(size):size+=2
        self.table=[None]*size
        self.count=0
    def exists(self,elt):
        key=hash(elt)
        index=key%len(self.table)
        start=index
        while True:
            if self.table[index]is None:return False
            elif self.table[index]and self.table[index]==elt:return True
            index=(index+1)%len(self.table)
            if index==start:return False
    def insert(self,elt):
        if self.exists(elt):return False
        key=hash(elt)
        index=key%len(self.table)
        start=index
        while True:
            if self.table[index]is None or self.table[index]is False:
                self.table[index]=elt
                self.count+=1
                return True
            index=(index+1)%len(self.table)
            if index==start:return False
    def delete(self,elt):
        if not self.exists(elt):return False
        key=hash(elt)
        index=key%len(self.table)
        start=index
        while True:
            if self.table[index]is None:return False
            elif self.table[index]and self.table[index]==elt:
                self.table[index]=False
                self.count-=1
                return True
            index=(index+1)%len(self.table)
            if index==start:return False
    def retrieve(self,elt):
        if not self.exists(elt):return False
        key=hash(elt)
        index=key%len(self.table)
        start=index
        while True:
            if self.table[index]is None:return None
            elif self.table[index]and self.table[index]==elt:return self.table[index]
            index=(index+1)%len(self.table)
            if index==start:return False
    def size(self):
        return self.count
    def __iter__(self):
        for elt in self.table:
            if elt: yield elt
