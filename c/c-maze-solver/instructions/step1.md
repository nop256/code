Maze solver
-----------

In this assignment you will implement a simple maze solver as well
as code to print out mazes. We will start with `print_maze`.


### Print

The maze is represented as a 2-dimensional array. The dimensions of
the array (the X size and Y size) are defined in `solve.h` and are
constants. `main` creates an array and reads a maze in from standard
in, and the maze is reprsented using one `char` value per square.
Here is a simple example maze:

```
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
....@.....@.@.@.@.....@.....@.@
@@@.@.@@@@@.@.@.@@@.@@@.@@@@@.@
@.@.@.........@.....@.....@...@
@.@.@@@@@.@.@@@.@.@@@@@.@@@.@@@
@.@.@.....@.....@.@.@.@...@...@
@.@.@@@@@.@@@.@@@@@.@.@.@@@.@@@
@.....@.@...@...@...........@.@
@.@.@@@.@.@@@@@@@@@.@@@@@.@@@.@
@.@.@.@.....@.@.@.......@.....@
@.@@@.@.@@@@@.@.@.@@@@@@@.@@@.@
@.....@.@...............@.@...@
@.@.@.@.@.@.@.@.@.@.@@@.@@@.@@@
@.@.@.....@.@.@.@.@...@.@......
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
```

A `@` character represents a wall, and a `.` character represents a
path. The maze always starts at the top left and ends at the bottom
right.

In this example maze the size is 31 across and 15 down, so it would
be represented with the array:

``` c
char field[15][31];
```

but you should always use the values `SIZE_Y` and `SIZE_X` as
defined in `solve.h`:

``` c
char field[SIZE_Y][SIZE_X];
```

The `print_maze` function is given the array as its only input, and
it should print the characters out to the screen with a newline at
the end of each row. You can use `printf` for this, or you can use
`putchar`, which is a more specialized function that prints a single
character (run `man putchar` for details).
