                .global _start
                .equ    sys_exit, 93
                .equ    thermostat_args, 1

                .data
msg_calling:    .asciz  "Calling thermostat with input => "
msg_got:        .asciz  "  thermostat returned =========> "
msg_newline:    .asciz  "\n"

                .balign 8
inputs:         .8byte  -5, -1, 0, 1, 5, 32, 60
                .8byte 66, 67, 68, 69, 70
                .8byte 73, 74, 75, 76, 77
                .8byte 80, 99, 100, 115, 1000000
                .equ    test_count, 22

                .text
_start:
                .option push
                .option norelax
                la      gp, __global_pointer$
                .option pop

                # for i = 0; i < 22; i++
                li      s0, 0
1:              li      t0, test_count
                bge     s0, t0, 2f

                # temp = inputs[i]
                la      t0, inputs
                slli    t1, s0, 3
                add     t2, t0, t1
                ld      s1, (t2)

                # print "calling" message including temp
                la      a0, msg_calling
                jal     print_string
                mv      a0, s1
                jal     print_int
                la      a0, msg_newline
                jal     print_string

                # print "returned" message prefix
                la      a0, msg_got
                jal     print_string

                # jal  the thermostat function
                mv      a0, s1
                jal     thermostat

                # report on its return value
                jal     print_int
                la      a0, msg_newline
                jal     print_string

                # i++, continue loop
                addi    s0, s0, 1
                j       1b

2:              li      a0, 0
                li      a7, sys_exit
                ecall
