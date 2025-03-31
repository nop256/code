Pencil marks: getting the set of used values
--------------------------------------------

In this step you will begin calculating pencil marks for a single
group by implementing the function `get_used` in the file
`pencil_marks.s`:

    get_used(board, group) -> used

where `board` and `group` are pointers to the entire board and a
single row of the lookup table, respectively, as described above.

When you start calculating the pencil marks, solved squares will
each have a single bit set to identify the number in that square.
Unsolved squares will have all 9 bits set (in positions 1–9, the
binary value 0b0000001111111110, or hex 0x03fe, or decimal 1022). In
this step you will scan the nine positions of the group and collect
the set of all solved values (the “used” values). In the next step
you will cross these values off the pencil markings of unsolved
squares, but for now you will just collect the list.

The high-level approach of this function is:

*   Scan the nine positions of the group
*   For each square, count the number of set bits in positions 1–9
*   If the count is one, it represents a solved square, so add the
    number to the “used” list
*   Return the “used” list as a set with one bit per used number

For the example row from earlier:

    +-----------------------+-----------------------+-----------------------+
    |       | . . . | . 2 . | . 2 . |       | . 2 . |       | . 2 . |       |
    |   1     4 . .   4 . . | . . .     3     4 . . |   5     . . .     6   |
    |       | 7 . 9 | 7 . 9 | 7 8 . |       | . 8 9 |       | . 8 9 |       |
    | - - - + - - - + - - - | - - - + - - - + - - - | - - - + - - - + - - - |

This function should return:

*   0b0000000001101010 = 0x006a

where the bit positions 1, 3, 5, and 6 are all ones and all other
positions are zeros.

The following pseudo-code will help you get started:

```
get_used(board, group) -> used
    used = 0
    for group_index = 0; group_index < 9; group_index++
        board_index = group[group_index]
        element = board[board_index]

        # note: looking up an element (the two lines above)
        # is really a 5-step process detailed here:
        group_element_address = group + group_index
        board_index = lb (group_element_address)
        scaled_board_index = board_index << 1
        board_element_address = board + scaled_board_index
        element = lh (board_element_address)

        # count the number of set bits in the element
        count = count_bits(element)

        if count == 1 (indicating a solved square):
            used = used | element

    return used
```

Note that this is a non-leaf function, so you will need to set up a
stack frame.

When you run `make` to test this, it will test your code on a
series of Sudoku puzzles. For each it will print the board to the
screen, then call your code on a sample of rows, columns, and boxes.
It will identify the group used, so you can examine it by hand to
verify the correct set of solved squares. It will then print the
result of calling `get_used`, both as a single decimal integer and
as the set of digits that number represents.
