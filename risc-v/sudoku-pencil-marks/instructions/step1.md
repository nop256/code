Sudoku
======

In this project you will write part of a Sudoku solver in RISC-V
assembly language over the course of 4 steps. You are given a few
pieces of code to start:

*   A function to read a Sudoku board from stdin (typically the
    keyboard) into an internal board representation

*   A function to print a board to stdout (typically the screen)
    complete with pencil markings

*   A `_start` function that will be updated with each step to test
    the code you are writing

Over the course of four steps you will implement one main feature:

A pencil mark calculator. In each unsolved square on the Sudoku
board, you will calculate which numbers are viable candidates to
solve the square. A viable candidate is any digit not already
present in a solved square in the same row, column, or box. A
standard technique for people solving Sudoku puzzles using
pencil and paper is to write the candidates out in each square
and then work to eliminate them until only one remains.

These instructions (and the instructions for other steps) will be
available in the `instructions` directory throughout this project.
You may find it helpful to refer back to the documentation for
earlier steps as you progress through the project.


Pencil marks and the board representation
-----------------------------------------

We will represent a Sudoku board as an array of 81 integers, each 16
bits in size (so the whole board will be 162 bytes long). The board
will be stored in *row-major order*, meaning that the first row will
be the first nine elements of the array, the second row the nine
elements after that, etc.

Within each square, the bits of the value will represent the pencil
marks (the viable candidates) for that square using bits 1–9 of the
16-bit number (we will not use bit 0 or bits 10–15). For each bit at
position *n*, a one will mean that *n* is a viable candidate and a
zero will mean that *n* is not viable. A square with only one viable
candidate is a solved square.

Here is an example row from a puzzle with pencil marks filled in:


    +-----------------------+-----------------------+-----------------------+
    |       | . . . | . 2 . | . 2 . |       | . 2 . |       | . 2 . |       |
    |   1     4 . .   4 . . | . . .     3     4 . . |   5     . . .     6   |
    |       | 7 . 9 | 7 . 9 | 7 8 . |       | . 8 9 |       | . 8 9 |       |
    | - - - + - - - + - - - | - - - + - - - + - - - | - - - + - - - + - - - |

None of the pencil marks include 1, 3, 5, or 6, since these are all
direct conflicts with solved squares within the same row. Each set
of pencil marks is different because they also account for conflicts
from the column and box that each square occupies. The above row is
represented as these nine values:

1.  0b0000000000000010 = 0x0002
2.  0b0000001010010000 = 0x0290
3.  0b0000001010010100 = 0x0294
4.  0b0000000110000100 = 0x0184
5.  0b0000000000001000 = 0x0008
6.  0b0000001100010100 = 0x0314
7.  0b0000000000100000 = 0x0020
8.  0b0000001100000100 = 0x0304
9.  0b0000000001000000 = 0x0040

This project will require extensive use of bit shifting and bitwise
operations to manipulate the squares. are treating a square as a set
of bits numbered 1–9 and using bitwise AND and OR operations to
implement set intersection and set union operations, respectively.
To review:

*   To test if a value *n* is in a set, shift 1 left *n* times to
    create a set containing only *n*. Then intersect (AND) it with
    the set and check if the result is empty (zero). If it is, the
    value *n* was not in the set.

*   An alternative method is to shift the set right *n* times so the
    bit you are interested in testing is in the least significant
    bit position. Then you can AND it with 1 and check if the result
    is zero (indicating that bit was clear to begin with) or one
    (the bit was set).

*   To add a value *n* to a set, shift 1 left *n* times to create a
    set containing only *n*, then union (OR) it with the set to add
    it to the set.


The board lookup table
----------------------

You will frequently need to consider all elements in the same group,
i.e., within a single row, a single column, or a single box. To
simplify this process, you are given a lookup table with the
following format:

    00 01 02 03 04 05 06 07 08
    09 10 11 12 13 14 15 16 17
    18 19 20 21 22 23 24 25 26
    ... (6 more rows)
    00 09 18 27 36 45 54 63 72
    01 10 19 28 37 46 55 64 73
    02 11 20 29 38 47 56 65 74
    ... (6 more columns)
    00 01 02 09 10 11 18 19 20
    03 04 05 12 13 14 21 22 23
    06 07 08 15 16 17 24 25 26
    ... (6 more boxes)

It is a table with 27 rows, each containing 9 numbers. Rows int the
first group each contain the index values of a rows on a Sudoku
board. The first row:

    00 01 02 03 04 05 06 07 08

gives the index values in a complete board of the elements of the
first row. The second lookup table row

    09 10 11 12 13 14 15 16 17

gives the index values of the elements of the second row, etc.

The second group repeats this but each row gives the index values of
a single column in the board. The first such row

    00 09 18 27 36 45 54 63 72

gives the index values of the elements of the first column, while
the second row in this group

    01 10 19 28 37 46 55 64 73

lets you easily look up the elements of the second column, etc.

The third and final group of rows in the lookup table helps look up
the elements in a single 3×3 box. The first row

    00 01 02 09 10 11 18 19 20

gives the index values of the elements in the first 3×3 box, the
second row of this part of the lookup table

    03 04 05 12 13 14 21 22 23

gives the index values of the elements of the second box, etc.

This table lets you easily work with all of the 27 logical groupings
on a Sudoku board. Say you want to process each of the 27 groups:

    for group_start = 0; group_start < 27*9; group_start += 9
        process_group(board, lookup_table+group_start)

In this example, `process_group` would be given the board and a
pointer to the beginning of a single row in the lookup table. Using
that row, it can easily find the nine elements of a row, column, or
box, but it does not need to know which group it is processing or
even the shape of that group. It can use the lookup table like this:

    process_group(int16_t *board, int8_t *group)
        for group_index = 0; group_index < 9; group_index++
            board_index = group[group_index]
            element = board[board_index]
            ...

You will use this pattern in several parts of this project.


Pencil marks: count the set bits
--------------------------------

Write a function in `pencil_marks.s` called `count_bits` with the
following function signature:

    count_bits(n) -> # of bits set in n (only counting bits 0–9 inclusive)

It should count the number of set bits in positions 0 through 9
inclusive. For example, if it is called with the following value as
input:

    0b01011011011

it should return 7. If called with this:

    0b11011011011

it should still return 7, because it only counts the 10
least-significant bits.

You can test if a single bit is set by shifting *n* right `index` times
for each value of `index` from 0 to 9 inclusive and then ANDing
that value with 1 and testing if the result is non-zero:

    count_bits(n) -> # of bits
        count = 0
        index = 0
        while index <= 9:
            temp = n>>index
            bit = temp&1
            if bit != 0:
                count += 1
            index += 1
        return count
