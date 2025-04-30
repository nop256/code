def delete(current, elt, exists):
    if not exists(elt): return False, current
    return True, deleteR(elt,current)
def deleteR(elt, current):
    if current is None: return None
    if elt < current.elt: current.l = self.deleteR(elt, current.l)
    elif elt > current.elt: current.r = self.deleteR(elt, current.r)
    else:
        if current.l is None and current.r is None: return None
        elif current.l is None: return current.r
        elif current.r is None: return current.l
        successor = current.r
        while successor.l is not None:
            successor = successor.l
        current.elt = successor.elt
        current.r = self.deleteR(successor.elt, current.r)
    return current

