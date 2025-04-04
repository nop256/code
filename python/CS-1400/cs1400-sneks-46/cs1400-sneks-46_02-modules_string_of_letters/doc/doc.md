# 46.2) A String of Letters

The `string` module has a variable named `ascii_letters`. Import this variable,
and use it to write the function `starts_with_letter` that consumes a word (as a
non-empty string) and returns whether the first character of that word is a
letter (as opposed to a number or symbol). Remember to unit test your function.

Technically, this function violates our scope rules - however, it is okay
because we are not changing the value inside letters (it's a global constant).
