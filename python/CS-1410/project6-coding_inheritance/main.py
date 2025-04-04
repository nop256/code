


from child1 import Smartphone
from child2 import Laptop
from child3 import FoldableSmartphone
from child4 import Inventory
from parent import Electronics

def main():
    InventoryList = []
    I1 = Inventory() #Initializing the Inventory instance

    #Making the Laptop object
    l1 = Laptop()
    l1.power_on()
    l1.power_off()
    l1.install_software('Thonny',3)
    InventoryList.append(l1)

    #Making a 2nd unique Laptop object
    l2 = Laptop(69, 32, 1024)
    l2.power_on()
    l2.power_off()
    l2.install_software('Valve',4)
    InventoryList.append(l2)

    #Making the Smartphone object
    s1 = Smartphone()
    s1.power_on()
    s1.power_off()
    s1.checkStorage()
    s1.installApp('Angry Birbs', 2.8)
    s1.checkApps()
    s1.uninstallApp('Angry Birbs')
    s1.adjustBrightness(49)
    InventoryList.append(s1)

    #Making a 2nd unique Smartphone object
    s2 = Smartphone()
    s2.power_on()
    s2.power_off()
    s2.checkStorage()
    s2.installApp('Happy Birbs', 2.8)
    s2.installApp('Furious Birbs', 3.2)
    s2.checkApps()
    s2.uninstallApp('Happy Birbs')
    s2.adjustBrightness(49)
    InventoryList.append(s2)

    #Making the FoldableSmartphone object
    f1 = FoldableSmartphone()
    f1.power_off()
    f1.power_on()
    f1.installApp('Flappy Birb',3.9)
    f1.checkStorage()
    f1.checkApps()
    f1.uninstallApp('Flappy Birb')
    f1.checkStorage()
    f1.adjustBrightness(100)
    f1.toggleFold()
    InventoryList.append(f1)

    #Making the Electronics object
    e1 = Electronics()
    e1.power_on()
    e1.power_off()
    InventoryList.append(e1)

    I1.add_item(l1)
    I1.add_item(s1)
    I1.add_item(f1) #Over the default limit of 2, should not add.
    I1.add_item(e1) #Over the default limit of 2, should not add.
    #print(I1.items)
    #print(I1) #Inventory should only contain 2 objects.

    for obj in InventoryList:
        print(obj.to_string())

main()
