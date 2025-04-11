
"""
class student:
    def __hash__(self):
        self.ssn.replace(
"""
#implemented as a hash table
#resizeable?
class bag:
    def __init__(self, expectedSize):
        """make table a set size, when it gets 2/3's full make another one twice as big as what it was, remove expectedSize"""
        actualSize=expectedSize * 2 + 1
        while not isprime(actualSize): # take square root of it, try all numbers through the square root...
            actualSize += 2
        self.table=[None]*actualSize

    def exists(self, int:item): # have to as item to represent itself as an integer
        key=hash(item)
        index=key%len(self.table)
 # if comparing one student to another, use '==' if comparing something to 'None' use 'is'
        while True:
            if self.table[index] is None: return False
            if self.table[index] and  self.table[index]==item: return True #IF object at index, and object is item, then return True. "Possible for index to be the item, but False.

            #They will all have this kind of a wrap
            index+=1
            if index >= len(self.table): index=0
