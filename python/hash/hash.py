

#implemented as a hash table
class bag:
    def __init__(self, expectedSize):
        """make table a set size, when it gets 2/3's full make another one twice as big as what it was, remove expectedSize"""
