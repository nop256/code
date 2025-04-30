Count letters
-------------

In the file `letters.c` write a function with the following
prototype:

    void letters_used(char *line);

Given a line of text, it should report on which letters are used in
the line. It should count upper- and lower-case letters, and should
report by printing the letters used in alphabetical order and in
lower case. For example, given the the following input as a single
line:

    When Mr Bilbo Baggins of Bag End announced that he would shortly
    be celebrating his eleventyifirst birthday with a party of
    special magnificence, there was much talk and excitement in
    Hobbiton.

It should print this output (including a newline at the end):

    abcdefghiklmnoprstuvwxy


Hints
-----

Remember that characters in C are just numbers. To check if a
character is a letter you can check if it is between 'a' and 'z' or
between 'A' and 'Z'. You can also use the `isalpha` function in the
standard library. Run “man isalpha” for help.

To convert an upper-case letter to lower-case you can use the
`tolower` function in the standard library. Run “man tolower” for
help.

One approach to this problem is to keep an array of booleans, one
for each letter or each ASCII character (there are 128 characters in
ASCII). You can use the letter itself (which is just a number) as
the index into the array. Initialize them all to false, then as you
scan the input you can set the array entry corresponding to each
letter to true. Finally, loop over the array entries corresponding
to letters and print out each letter whose entry is set to true.
