

from child1 import Smartphone
from child2 import Laptop
from child3 import FoldableSmartphone
from parent import Electronics

class Inventory(Electronics):
    """
    A class representing an inventory of electronic devices.

    Attributes:
    ----------
    items : list
        A list to store Electronics objects.
    max_size : int
        Maximum number of items that the inventory can hold.

    Methods:
    -------
    add_item(item):
        Adds an electronic item to the inventory if there's space.
    remove_item(item):
        Removes an electronic item from the inventory.
    __str__():
        Returns a string representation of the items in the inventory.
    """
    def __init__(self,max_size=2):
        """
        Initializes the inventory with a maximum size and an empty list of items.

        Parameters:
        ----------
        max_size : int, optional
            Maximum number of items the inventory can hold (default is 10).
        """
        super().__init__()
        self.items = []
        self.max_size = max_size

    def add_item(self, item):
        """
        Adds an item to the inventory if there is enough space.

        Parameters:
        ----------
        item : Electronics
            The electronic item to be added.

        Returns:
        -------
        str
            A message indicating whether the item was added successfully or not.
        """
        if len(self.items) < self.max_size:
            self.items.append(item)
            return f"Item added: {str(item)}"
        else:
            return "Inventory is full, cannot add more items."

    def to_string(self):
        """
        Returns a string representation of all items in the inventory.

        Returns:
        -------
        str
            A summary of the items currently in the inventory.
        """
        if not self.items:
            return "Inventory is empty."
        item_list = "\n".join([super().to_string() for item in self.items])
        return f"Inventory contains:\n{item_list}"

if __name__ == "__main__":
    I1 = Inventory() #Initializing the Inventory instance

    #Making the Laptop object
    l1 = Laptop()
    print(l1.power_on())
    print(l1.power_off())
    print(l1.install_software('Thonny',3))
    #print(l1)

    #Making the Smartphone object
    s1 = Smartphone()
    print(s1.power_on())
    print(s1.power_off())
    print(s1.checkStorage())
    print(s1.installApp('Angry Birbs', 2.8))
    print(s1.checkApps())
    print(s1.uninstallApp('Angry Birbs'))
    print(s1.adjustBrightness(49))
    #print(s1)

    #Making the FoldableSmartphone object
    f1 = FoldableSmartphone()
    print(f1.power_off())
    print(f1.power_on())
    print(f1.installApp('Flappy Birb',3.9))
    print(f1.checkStorage())
    print(f1.checkApps())
    print(f1.uninstallApp('Flappy Birb'))
    print(f1.checkStorage())
    print(f1.adjustBrightness(100))
    print(f1.toggleFold())
    #print(f1)

    #Making the Electronics object
    e1 = Electronics()
    print(e1.power_on())
    print(e1.power_off())
    #print(e1)

    print(I1.add_item(l1))
    print(I1.add_item(s1))
    print(I1.add_item(f1)) #Over the default limit of 2, should not add.
    print(I1.add_item(e1)) #Over the default limit of 2, should not add.
    print(I1.items)
    #print(I1) #Inventory should only contain 2 objects.
    print(I1.to_string())
