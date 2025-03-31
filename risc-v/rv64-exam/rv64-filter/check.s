                .global check, min_value
                .text
                .equ    check_args, 1

check:          ld      t0, min_value
                slt     a0, a0, t0
                xori    a0, a0, 1
                ret

                .data
                .balign 8
min_value:      .8byte  0
