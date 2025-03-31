### Solve

To solve the maze we will use a technique from *cellular logic*. The
approach is to look at each position on the field and decide whether
or not to change it based only on the positions immediately
surrounding it.

Here is the big idea of this solver: we will define a simple dead
end as a path that is surrounded on three sides (up, down, left,
right) by walls. A simple dead end can never be part of the solution
to the maze, so we turn it into a wall instead. This may create a
new simple dead end, so we repeat the process until there are no
simple dead ends left on the maze. What is left is a field of all
walls except for the solution path, which remains intact.

A few important details:

1.  Scan the entire field looking for simple dead ends. Use a pair
    of nested loops to scan every position on the board.

2.  Be careful not to scan outside the boundaries of the maze,
    i.e., never do an array lookup that would look past the left,
    right, top, or bottom edges of the maze.

3.  At each position, check if:

    a)  The position is a path character
    b)  There are exactly three neighbors that are walls

    If so, replace the path with a wall.

4.  After completing a sweep over the entire field (except the very
    edges as noted above), start over if you made any changes.

5.  Return when you have made a complete pass over the field and not
    made any changes.

With each pass over the field, the dead ends will get shorter and
shorter until eventually there are none left.

To test, you might find it helpful to call `print_maze` at various
times to see if the effect is working. For example, make only a
single pass over the field and then call `print_maze`. Look at the
results and see if the dead ends are getting shorter. Be sure to
remove debugging code before you finish.

You will probably want to test this by calling it directly as
described earlier so you can see the complete output even when it is
incorrect. Once you are confident everything is working, run `make`
to get the full test results, and then move on to `grind grade` to
submit your code for grading.


Making new mazes
----------------

Build your code as before, but generate a fresh new maze to feed
to it. I have included a Python program that generates a fresh
maze each time it is called. It uses a terrible maze algorithm,
but it works:

    python3 makemaze.py | ./a.out

This tells the Linux shell to run the `makemaze.py` program and
to connect its output to the input of `a.out`.
