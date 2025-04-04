Exercise: missing_char
----------------------

### Description

In this exercise, your function will receive two parameters.
The first is a string, and the second is an index into
the string.  The function returns a copy of the string
without the character at the index specified.

### Function Name

missing_char

### Parameters

* `string` : a string value
* `index` : an integer value (a legal index for `string`)

### Return Value

A copy of `string`, with `string[index]` missing.

### Examples

    missing_char("fred", 0) -> "red"
    missing_char("fred", 1) -> "fed"
    missing_char("fred", 2) -> "frd"
    missing_char("fred", 3) -> "fre"
