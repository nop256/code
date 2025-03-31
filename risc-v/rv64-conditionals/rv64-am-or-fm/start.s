                .global _start
                .equ    sys_exit, 93
				.equ	am_or_fm_args, 1

                .data
msg_calling:    .asciz  "Calling am_or_fm with input => "
msg_got:        .asciz  "  am_or_fm returned =========> "
msg_newline:    .asciz  "\n"
msg_end:

                .balign 8
inputs:         .8byte  535, 536, 1000, 1604, 1605
                .8byte  88, 89, 98, 107, 108
                .8byte  0, -1, -535, -88, 534, 1606, 87, 109, 500, 10000, 50
inputs_end:
                .equ    test_count, 21

                .text
_start:
                .option push
                .option norelax
                la      gp, __global_pointer$
                .option pop

                # for i = 0; i < 21; i++
                li      s0, 0
1:
                la      t0, inputs
                slli    t1, s0, 3
                add     t2, t0, t1
                ld      s1, (t2)
                la      a0, msg_calling
                call    print_string
                mv      a0, s1
                call    print_int
                la      a0, msg_newline
                call    print_string
                la      a0, msg_got
                call    print_string
                mv      a0, s1
                call    am_or_fm
                call    print_int
                la      a0, msg_newline
                call    print_string
                addi    s0, s0, 1
                li      t0, test_count
                blt     s0, t0, 1b

                li      a0, 0
                li      a7, sys_exit
                ecall
