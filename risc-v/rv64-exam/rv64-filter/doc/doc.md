Filter
======

Write a RISC-V function to copy some values from an array into
another array:

    filter(int *in_start, int *in_end, int *out_start) -> int *out_end

`filter` is given the address of the beginning of an array
(`in_start`), the end of that array (`in_end`). It should copy some
of the values from that array into a new array at address
`out_start` and return the address of the end of that array when it
is finished.

For each element of the input array, it should call the function
`check` to decide if that element should be copied or ignored. If
`check` returns zero the array element should be skipped, and if it
returns non-zero it should copy that element to the output array.

So it should implement something like this:

    def filter(in_start, in_end, out_start):
        while in_start < in_end:
            # load the element from address in_start
            elt = *in_start

            # see if we should copy it
            keep = check(elt)
            if keep != 0:
                # write the element to out
                *out_start = elt

                # increment out_start (this adds 8 to the address
                # due to pointer arithmetic)
                out_start += 1

            # increment in_start (adds 8 to the pointer)
            in_start += 1

        # out_start is now the end of the output array
        return out_start

Note that `filter` is not a leaf function so you should set up a
stack frame so that you can safely call `check`.

Write your code in `filter.s`
