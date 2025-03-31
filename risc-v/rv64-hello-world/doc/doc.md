The purpose of this assignment is to make sure your build
environment is set up correctly.

Edit the file hw.s so that it loads the number 42 into register a0
before returning. This can be accomplished with a single added
instruction:

    li  a0, 42

To test the code:

    make

This does a few things. It builds the project, it runs it, and it
watches the output and compares it with the expected output. If
everything is correct it will simply run to completion. If there is
anything incorrect in the output it will stop and show both what
your code displayed (the actual output) and what it should have
displayed (the expected output).

You can also run the run without checking the output:

    make run

When everything is working correctly, submit your code for grading:

    grind grade
