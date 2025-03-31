                .global _start
                .equ    sys_exit, 93
                .equ    gcd_args, 2

                .data
                .balign 8
inputs:         .quad   15, 5, 28, 7, 36, 60, 101, 10, 37, 18
                .quad   48, 180, 100, 200, 105, 60, 987, 111, 91, 364
                .quad   198, 14, 56, 42, 21, 14, 69, 51, 144, 72
                .quad   91, 104, 150, 300, 462, 1071, 156, 39, 98, 56
                .equ    test_count, 20

msg_calling:    .asciz  "Calling gcd("
msg_comma:      .asciz  ","
msg_got:        .asciz  ")\n  return value is ========> "
msg_newline:    .asciz  "\n"

                .text
_start:
                .option push
                .option norelax
                la      gp, __global_pointer$
                .option pop

                li      s0, 0
                la      s1, inputs

                # main test loop
1:              li      t0, test_count
                bge     s0, t0, 2f

                # load the inputs
                ld      s2, (s1)
                addi    s1, s1, 8
                ld      s3, (s1)
                addi    s1, s1, 8

                # print the messages
                la      a0, msg_calling
                jal     print_string
                mv      a0, s2
                jal     print_int
                la      a0, msg_comma
                jal     print_string
                mv      a0, s3
                jal     print_int
                la      a0, msg_got
                jal     print_string

                # call gcd
                mv      a0, s2
                mv      a1, s3
                jal     gcd

                # print result
                jal     print_int
                la      a0, msg_newline
                jal     print_string

                # continue loop
                addi    s0, s0, 1
                j       1b

2:              li      a0, 0
                li      a7, sys_exit
                ecall
