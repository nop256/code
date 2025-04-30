Format phone numbers
--------------------

In the file `phonenumber.c` write a function with the following
prototype:

    void format_phone_number(char *line);

It is given a line of input with a 10-digit phone number, and it
should format and print that phone number in this format:

    (435) 652-5000

If the input is invalid, it should instead print the message:

    Invalid input

The input has a few rules to be considered valid:

*   The area code (the first three digits) must appear as a group of
    three digits with no spaces or punctuation between them.
*   The prefix (the next three digits) must also appear as a group
    with nothing breaking up the three digits.
*   The line number (the last four digits) must appear as a group.
*   Any number of non-digits may appear before the area code,
    between the area code and the prefix, between the prefix and the
    line number, or after the line number, but no extra digits are
    permitted.

So, for example, the following are valid inputs:

    (435) 555-1698
    801-123-9876
    9874327654

But the following are not valid:

    (435) 555-16982
    801-1239-876
    8-0-1-1-2-3-9-8-7-6

Your function should print one line of output in the correct format
(or the "Invalid input" message) followed by a newline.


Hints
-----

Avoid `sscanf` and similar functions for this problem. They are
great when you know the precise format of the input, but are not
well suited to a problem like this where you need to be flexible
about the input.

Instead, treat your input an a simple array of characters. Starting
at the beginning of the string, follow a sequence like this:

*   Skip over all the non-digits at the beginning of the string
*   Check if there are exactly 3 digits in a row for the area code
    and remember where they are/copy them.
*   Skip over any non-digits after the area code.
*   Check if there are exactly 3 digits in a row for the prefix
    code and remember where they are/copy them.
*   Skip over any non-digits after the prefix.
*   Check for exactly 4 digits for the line number and remember
    them/copy them.
*   Skip over any non-digits after the line number.
*   Make sure you have reached the end of the string.

To check for a sequence of digits you can use something like:

    if (isdigit(line[i]) && isdigit(line[i+1]) && isdigit(line[i+2]))

One you have located the groups of digits and validated them, print
the three groups of digits with the correct format.
