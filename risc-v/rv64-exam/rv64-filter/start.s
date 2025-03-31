                .global _start
                .text
                .equ    sys_exit, 93
                .equ    filter_args, 3

_start:
                .option push
                .option norelax
                la      gp, __global_pointer$
                .option pop

                # empty input list
                la      a0, test_array_1
                la      a1, test_array_1
                li      a2, -1
                jal     run_test

                # list with one element: 5
                la      a0, test_array_1
                la      a1, test_array_2
                li      a2, 10
                jal     run_test

                la      a0, test_array_1
                la      a1, test_array_2
                li      a2, 0
                jal     run_test

                la      a0, test_array_1
                la      a1, test_array_2
                li      a2, 5
                jal     run_test

                la      a0, test_array_1
                la      a1, test_array_2
                li      a2, 6
                jal     run_test

                # list with 10 elements: 2, 13, 16, 24, 5, 7, 11, 10, 6, 13

                la      a0, test_array_2
                la      a1, output_array
                li      a2, 0
                jal     run_test

                la      a0, test_array_2
                la      a1, output_array
                li      a2, 2
                jal     run_test

                la      a0, test_array_2
                la      a1, output_array
                li      a2, 3
                jal     run_test

                la      a0, test_array_2
                la      a1, output_array
                li      a2, 10
                jal     run_test

                la      a0, test_array_2
                la      a1, output_array
                li      a2, 13
                jal     run_test

                la      a0, test_array_2
                la      a1, output_array
                li      a2, 14
                jal     run_test

                # exit
                li      a0, 0
                li      a7, sys_exit
                ecall

run_test:
                addi    sp, sp, -32
                sd      ra, 24(sp)
                sd      s0, 16(sp)
                sd      s1,  8(sp)
                sd      s2,  0(sp)

                mv      s0, a0
                mv      s1, a1
                mv      s2, a2

                la      a0, msg_filter
                jal     print_string
                mv      a0, s2
                jal     print_int
                la      a0, msg_in
                jal     print_string
                mv      a0, s0
                mv      a1, s1
                jal     print_int_list
                la      a0, msg_out
                jal     print_string

                sd      s2, min_value, a2
                mv      a0, s0
                mv      a1, s1
                la      a2, output_array
                jal     filter

                mv      a1, a0
                la      a0, output_array
                jal     print_int_list
                la      a0, newline
                jal     print_string

                ld      ra, 24(sp)
                ld      s0, 16(sp)
                ld      s1,  8(sp)
                ld      s2,  0(sp)
                addi    sp, sp, 32
                ret

print_int_list:
                addi    sp, sp, -32
                sd      ra, 24(sp)
                sd      s0, 16(sp)
                sd      s1,  8(sp)
                sd      s2,  0(sp)

                mv      s0, a0
                mv      s1, a1
                la      s2, sep_empty
1:              bge     s0, s1, 2f
                mv      a0, s2
                jal     print_string
                la      s2, sep_comma
                ld      a0, (s0)
                jal     print_int
                addi    s0, s0, 8
                j       1b

2:              ld      ra, 24(sp)
                ld      s0, 16(sp)
                ld      s1,  8(sp)
                ld      s2,  0(sp)
                addi    sp, sp, 32
                ret

                .data
                .balign 8
msg_filter:     .asciz  "\nfilter to just the values >= "
msg_in:         .asciz  "\ninput : "
msg_out:        .asciz  "\noutput: "
newline:        .asciz  "\n"
sep_empty:      .asciz  ""
sep_comma:      .asciz  ", "

                .balign 8
test_array_1:   .8byte  5
test_array_2:   .8byte  2, 13, 16, 24, 5, 7, 11, 10, 6, 13
output_array:   .8byte  0, 0, 0, 0, 0, 0, 0, 0, 0, 0
output_array_end:
