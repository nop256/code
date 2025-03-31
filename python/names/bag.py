class Bag:
    """A container class that stores unique items in an unordered manner."""

    def __init__(self):
        """Initialize an empty list to store items."""
        self.bag = []

    def insert(self, item):
        """Insert an item into the bag if it does not already exist."""
        if self.exists(item):
            return False
        else:
            self.bag.append(item)
            return True
        
    def retrieve(self, item):
        for obj in self.bag:
            if item == obj:
                return obj
        return None
    
    def delete(self, item):
        for obj in self.bag:
            if obj == item:
                self.bag.remove(obj)
                return True
        return False
    
    def __iter__(self):
        for item in self.bag:
            yield item
        

    def exists(self, item):
        """Check if an item exists in the bag."""
        for obj in self.bag:
            if obj == item:
                return True
        return False

    def size(self):
        """Return the number of items in the bag."""
        return len(self.bag)
