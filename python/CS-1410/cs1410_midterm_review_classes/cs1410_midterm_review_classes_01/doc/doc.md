Exercise: Battery Constructor
-------------------------

### Description

In the next several exercises you will create
a class to represent the rechargeable battery.
The battery has a maximum capacity, and a current
charge.  It's values can be checked.  It can also
be recharged and drained of charge.

In this exercise, you will create a class to represent
a `Battery`, its capacity and its charge.  You are only
responsible for creating the data members to store
capacity and charge in the constructor.  The initial
charge of the battery should be set to the capacity.

### Files

* `battery.py` : Python with class definition

### Class Name

`Battery`

### Constructor

`__init__()`

### Parameters

* `self` : the `Battery` object to initialize
* `capacity` : a number, the maximum amount of charge the battery can hold

### Action

Initializes the data member for capacity from the parameter, and
the data member for charge from the capacity.

### Examples

    b = Battery(3080) -> b is a Battery object with capacity of 3080, and fully charged with 3080
