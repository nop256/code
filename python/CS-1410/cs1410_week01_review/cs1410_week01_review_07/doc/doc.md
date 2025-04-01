Exercise: sum13
---------------------

### Description

Return the sum of the numbers in the list, returning 0 for
an empty list.  Except the number 13 is very unlucky,
so it does not count and numbers that come immediately
after a 13 also do not count.      

### Function Name

sum13

### Parameters

* `nums` : a list of integers

### Return Value

The sum of `nums`, without 13s or numbers that immediately
follow 13s.

### Examples

    sum13([1, 2, 2, 1]) -> 6  
    sum13([1, 1]) -> 2  
    sum13([1, 2, 2, 1, 13]) -> 6
    sum13([1, 13, 99, 2, 2, 1]) -> 6

    
