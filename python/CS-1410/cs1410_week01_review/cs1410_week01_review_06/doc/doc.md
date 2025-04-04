Exercise: fifthchar
----------------------

### Description

In this exercise, your function will receive 1 parameter,
the name of a text file.  The function will return a string
created by concatenating the fifth character from each line
into one string.  If the line has fewer than 5 characters,
then the line should be skipped.  All lines should have
leading and trailing whitespace removed before looking for
the fifth character.

### Function Name

fifthchar

### Parameters

* `filename` : a string value (the name of a file to open)

### Return Value

A string made from the fifth character of each line that has at least 5 characters.

### Examples

    fifthchar("input.txt") -> skzke akeaa4

### Hint

What is the index of the fifth character in a string?  How can
you tell if there is a fifth character?
