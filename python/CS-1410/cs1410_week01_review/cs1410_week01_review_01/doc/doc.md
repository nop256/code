Exercise: partlist2
----------------------

### Description

In this exercise, your function will receive 3 parameters,
a list and two integers.  The function will return the
slice of the list starting from the index of the first
number and going to the end.
It will step through the list using the second number.

### Function Name

partlist2

### Parameters

* `nums` : a list value
* `a` : an integer value (the index to start at)
* `c` : an integer value (the step value)

### Return Value

A list starting at index `a` of `nums` and going to the end,
only including every `c`th element.

### Examples

    partlist2([ 2, 3, 5, 7, 11, 13 ], 1, 2) -> [ 3, 7, 13 ]
    partlist2([ 2, 3, 5, 7, 11, 13 ], 2, 3) -> [ 5, 13 ]

### Hints

Remember how to slice a list?
