Pencil markings: processing the entire board
--------------------------------------------

In this step you will calculate pencil markings for the entire board
using the helper functions from the previous steps. Implement the
function `pencil_marks` in the file `pencil_marks.s`:

    pencil_marks(board, table) ->
        0: no changes
        1: something changed

A Sudoku board has 27 groups comprised of nine rows, nine columns,
and nine 3×3 boxes. At a high level this function must

*   Loop over the 27 groups on the board
*   For each group, call `get_used` to calculate the used set, then
    call `clear_used` to cross those values off unsolved squares in
    the same group
*   If anything changed on the entire board, return true

This function is not a leaf function so you must use the stack to
store the return address and any saved registers that you need for
local variables. This function must also walk over the lookup table
to find the row corresponding to each group:

```
pencil_marks(board, table) -> 0: no changes, 1: something changed
    changed = 0
    for group_start = 0; group_start < 27*9; group_start += 9
        used = get_used(board, table+group_start)
        delta = clear_used(board, table+group_start, used)
        if delta != 0:
            changed = 1
    return changed
```

You must track if changes are made because calculating pencil marks
will sometimes solve squares by narrowing the set of possible values
down to one, which in our representation is equivalent to a solved
square. That may change the correct set of pencil marks for groups
that have already been processed, so to get a complete set of
correct pencil marks we may need to run `calc_pencil` multiple times
until no further changes are made. `_start` does this, so for some
of the test cases you will see `pencil_marks` called multiple times.
