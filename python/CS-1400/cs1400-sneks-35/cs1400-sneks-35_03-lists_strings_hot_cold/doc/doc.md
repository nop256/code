# 35.3) Hot and Cold

A scientist has been recording observations of the temperature for the past
while. On hot days, they write "H", and for cold days, they write "C". Instead
of using a list, they kept all of these observations in a single long string
(e.g., "HCH" would be a hot day, followed by a cold day, and then another hot
day).

Write a function `add_hot_cold` that consumes a string of observations and
returns the number of hot days minus the number of cold days. To accomplish
this, you should process each letter in turn and add 1 if it is hot, and -1 if
it is cold. For example, the string "HCH" would result in 1, while the string
"CHCC" would result in -2.

You cannot use the built-in `.count()` method or the `len()` function for this
problem.

Don't forget to unit test your function.
