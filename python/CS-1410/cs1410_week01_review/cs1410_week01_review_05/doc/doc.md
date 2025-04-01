Exercise: fourthchar
----------------------

### Description

In this exercise, your function will receive 2 parameters,
the name of a text file, and a list of strings.
The function will write one line to the text file.  The line
will contain the fourth character of every string in the list.
For any strings that don't have four characters, use `x`.
Be sure to include the newline character at the end.

### Function Name

fourthchar

### Parameters

* `filename` : a string value (the name of a file to open)
* `lines` : a list of string values

### Return Value

Nothing

### Examples

    fourthchar("output.txt", ["abcde","ghi","jklm"])
    # output.txt created with one line containing dxm

### Hint

What is the index of the fourth character in a string?  How can
you tell if there is a fourth character?
