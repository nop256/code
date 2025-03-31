Pencil markings: clearing used values from unsolved squares
-----------------------------------------------------------

In this step you will continue calculating pencil marks for a single
group by implement the function `clear_used` in the file
`pencil_marks.s`:

    clear_used(board, group, used) ->
        0: no changes
        1: something changed

where `board` and `group` are the same as in `get_used` and `used`
is a set of values used in solved squares (the same value returned
by `get_used`).

Here is an example input row with the same solved squares as before:

    +-----------------------+-----------------------+-----------------------+
    |       | 1 2 3 | 1 2 3 | 1 2 3 |       | 1 2 3 |       | 1 2 3 |       |
    |   1     4 5 6   4 5 6 | 4 5 6     3     4 5 6 |   5     4 5 6     6   |
    |       | 7 8 9 | 7 8 9 | 7 8 9 |       | 7 8 9 |       | 7 8 9 |       |
    | - - - + - - - + - - - | - - - + - - - + - - - | - - - + - - - + - - - |

If `clear_used` is called with the used set represented by

*   0b0000000001101010 = 0x006a

where the bit positions 1, 3, 5, and 6 are all ones and all other
positions are zeros and all unsolved positions have a full set of
pencil marks (as illustrated above), `clear_used` should change the
pencil marks in the row to be:

    +-----------------------+-----------------------+-----------------------+
    |       | . 2 . | . 2 . | . 2 . |       | . 2 . |       | . 2 . |       |
    |   1     4 . .   4 . . | 4 . .     3     4 . . |   5     4 . .     6   |
    |       | 7 8 9 | 7 8 9 | 7 8 9 |       | 7 8 9 |       | 7 8 9 |       |
    | - - - + - - - + - - - | - - - + - - - + - - - | - - - + - - - + - - - |

i.e., the values 1, 3, 5, and 6 have been “crossed off” the pencil
marks of all unsolved squares in the same group (row, column, or
box).

To clear some elements from a set we use *set difference*, normally
written as S-T, where the result is all elements in set S that are
not also in set T. S-T is equivalent to `S&(~T)`, i.e., S
intersected with the complement of T. Flipping the bits of `used`
(using the `not` instruction) will give us the complement of the set
it represents.

At a high level, this function will:

*   Loop over the nine positions of the group
*   For each square, count the set bits in positions 1–9
*   If the count is *not* 1, this represents an unsolved square so
    cross off all the elements from the `used` list
*   Note if anything actually changed and return true if so

The following pseudo-code is a starting point for implementing
`clear_used`:

```
clear_used(board, group, used) -> 0 or 1:
    notused = ~used (flip the bits)
    change_made = 0
    for group_index = 0; group_index < 9; group_index++
        board_index = group[group_index]
        elt = board[board_index] # remember the address

        count = count_bits(elt)

        if count != 1 (indicating an unsolved square):
            new_elt = elt & notused (clear the bits indicated by used)
            if new_elt != elt:
                board[board_index] = new_elt # use the address from earlier
                change_made = 1

    return change_made
```

Note that this is a non-leaf function.
