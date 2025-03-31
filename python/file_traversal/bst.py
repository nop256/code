class Node:
    def __init__(self,elt):
        self.elt = elt #pointer to the element itself
        self.l = None #pointer to left child elt
        self.r = None #pointer to right child elt

class Container:
    def __init__(self):
        self.root = None
    
    def exists(self, elt):
        return self.existsR(elt, self.root) #start recursion to check if element exists.
    
    def existsR(self, elt, current):
        if current is None: return False #element not found.
        elif elt == current.elt: return True #found the element.
        elif elt < current.elt: return self.existsR(elt, current.l) #search left.
        elif elt > current.elt: return self.existsR(elt, current.r) #search right.
    
    def insert(self, elt):
        if self.exists(elt): return False #element is duplicate, and cannot be added.
        self.root = self.insertR(elt, self.root) #start recursion to add elt to bst.
        return True
    
    def insertR(self, elt, current):
        if current is None: current = Node(elt) #if current node is empty, insert element here.
        elif elt < current.elt: current.l = self.insertR(elt, current.l) #element is lesser  than current, so look at the left child.
        elif elt > current.elt: current.r = self.insertR(elt, current.r) #element is greater than current, so look at the right child.
        return current
        
    def delete(self, elt):
        if not self.exists(elt): return False #if element does not exist in the tree, return False.
        self.root = self.deleteR(elt, self.root) #start recursion to delete the (existing) element.
        return True #element successfully deleted.
    
    def deleteR(self, elt, current):
        if current is None: return None #node is empty. Return (None) value unchanged.
        if elt < current.elt: current.l = self.deleteR(elt, current.l) #element is less than current. recur left
        elif elt > current.elt: current.r = self.deleteR(elt, current.r) #element is greater than current. recur right
        else: #node found. (elif elt == current.elt: )
            if current.l is None and current.r is None: return None #no children. return None to delete current node. (replaces current)
            elif current.l is None: return current.r #one right child found. bypass node by returning current.r. (replaces current)
            elif current.r is None: return current.l #one left child found. bypass node
            successor = current.r #two children exist. name the successor to replace the node to be deleted.
            while successor.l is not None: #search for the smallest node in the right subtree (left-max)
                successor = successor.l #successor reassigned to the left max of the right subtree
            current.elt = successor.elt #replace value of node to delete with the in-order left-max successor
            current.r = self.deleteR(successor.elt, current.r) #recursively deletes the in-order successor node (which was copied to current.elt)
        return current
    
    def __iter__(self):
        yield from self.IterRecursive(self.root)
        
    def IterRecursive(self, current):
        if current is not None:
            yield from self.IterRecursive(current.l)
            yield current.elt
            yield from self.IterRecursive(current.l)
    
    def retrieve(self, elt):
        return self.retrieveR(elt, self.root) #recurse retrieval of the element.
    
    def retrieveR(self, elt, current):
        if not self.exists(elt): return False #element does not exist.
        if current is None: return None #emement not found.
        if elt == current.elt: return current.elt #element found.
        elif elt < current.elt: return self.retrieveR(elt, current.l) #element is lesser  than current, so look at and/or left child.
        elif elt > current.elt: return self.retrieveR(elt, current.r) #element is greater than current, so look at and/or right child.
    
    def size(self):
        return self.sizeR(self.root) #recurse size counter
    
    def sizeR(self, current):
        if current is None: return 0 #node is empty, do not increment.
        return 1 + self.sizeR(current.l) + self.sizeR(current.r) #1 for the current node, recursively count all nodes in left and right subtrees.
    
    # every method = method + recursive counterpart