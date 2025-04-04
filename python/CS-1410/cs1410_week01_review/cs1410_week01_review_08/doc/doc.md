Exercise: combo_string
----------------------

### Description

Given 2 strings, `a` and `b`, return a string of the form
short+long+short, with the shorter string on the outside and
the longer string on the inside. The strings will not be the
same length, but they may be empty (length 0).

### Function Name

combo_string

### Parameters

* `a` : a string
* `b` : a string

### Return Value

A string in the form of short+long+short.

### Examples

    combo_string('Hello', 'hi') -> 'hiHellohi'  
    combo_string('hi', 'Hello') -> 'hiHellohi'  
    combo_string('aaa', 'b') -> 'baaab'
