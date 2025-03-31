                .global pencil_marks, get_used, clear_used, count_bits
                .text

# count_bits(n) -> # of bits set in n (only counting bits 0-9 inclusive)
count_bits:
	li	t0, 10		# loop counter
	li	t1, 0		# count
	li	t2, 1		# bitmask

loop_count:
	and 	t3, a0, t2		# extract least significant bit
	beqz 	t3, skip_count	# if bit is 0, skip incrementing

	addi	t1, t1, 1	# incremement count

skip_count:
	slli	t2, t2, 1	# shift mask left by 1 (next bit)
	addi	t0, t0, -1	# decrement loop counter
	bnez	t0, loop_count	# repeat until 10 bits are checked

	mv	a0, t1		# move the result (bit count) to a0 (return value)
	ret
#------------------------------------------------------------------
#get_used(board, group) -> used
#    used = 0
#    for group_index = 0; group_index < 9; group_index++
#        board_index = group[group_index]
#        element = board[board_index]
#
#        # note: looking up an element (the two lines above)
#        # is really a 5-step process detailed here:
#        group_element_address = group + group_index
#        board_index = lb (group_element_address)
#        scaled_board_index = board_index << 1
#        board_element_address = board + scaled_board_index
#        element = lh (board_element_address)
#
#        # count the number of set bits in the element
#        count = count_bits(element)
#
#        if count == 1 (indicating a solved square):
#            used = used | element
#
#    return used
#------------------------------------------------------------------
get_used:
	#prologue
	addi	sp, sp, -48
	sd	ra, 40(sp)	# save return address
	sd	s0, 32(sp)	# 'board
	sd	s1, 24(sp)	# 'group_index'
	sd	s2, 16(sp)	# 'group'
	sd	s3, 8(sp)	# 'element'
	sd	s4, 0(sp)	# 'used'
	
	#----------------------------------------------------------	
	# Map:
	# s0 = board
	# s1 = group index
	# s2 = group
	# s3 = element
	# s4 = used
	#
	# t0 = compare value
	# t1 = group_element_address
	# t2 = board_index
	# t3 = scaled_board_index
	# t4 = board_element_address
	# t5 = bit_count
	#----------------------------------------------------------

	li	s4, 0		# used = 0
	li	s1, 0		# group_index = 0
	mv	s0, a0		# s0 = board
	mv	s2, a1		# s2 = group

loop_group:
	li	t0, 9		# loading 9 into t0 to compare with s1
	bge	s1, t0, done_group	# if s1 >= t0: goto done
	
	# calculate board index
	add	t1, s2, s1	# group_element_address = group + group_index
	lbu	t2, 0(t1)	# board_index = lb(group_element_address)
	
	# calculate board_element_address
	slli	t3, t2, 1	# scaled_board_index = board_index << 1
	add	t4, s0, t3	# board_element_address = board + scaled_board_index
	lhu	s3, 0(t4)	# element = lh (board_element_address)

	# count the number of set bits in the element
	# count = count_bits(element)
	mv	a0, s3		# setting a0 as the output argument for count_bits
	jal	count_bits	# returns bit count in a0
	mv	t5, a0		# stores bit count in a6
	
	# if bit_count == 1, OR the original element into 'used':
	li	t0, 1
	bne	t5, t0, skip_or
	or	s4, s4, s3
	
skip_or:
	addi	s1, s1, 1	# group_index ++
	j	loop_group

done_group:
	mv	a0, s4		# return 'used' in a0

	# epilogue
	ld	ra, 40(sp)
	ld	s0, 32(sp)
	ld	s1, 24(sp)
	ld	s2, 16(sp)
	ld	s3, 8(sp)
	ld	s4, 0(sp)
	addi	sp, sp, 48
	ret

# ------------------------------------------------------------------------------
# clear_used(board, group, used) -> 0 or 1
#
# Pseudocode:
#    notused = ~used
#    change_made = 0
#    for group_index in [0..8]:
#        board_index = group[group_index]
#        elt = board[board_index]
#
#        count = count_bits(elt)
#
#        if (count != 1):
#            new_elt = elt & notused
#            if new_elt != elt:
#                board[board_index] = new_elt
#                change_made = 1
#
#    return change_made
# ------------------------------------------------------------------------------
# clear_used(board, group, used)
clear_used:
	# Prologue:
	addi	sp, sp, -64

	sd      ra, 56(sp)
        sd      s0, 48(sp)
        sd      s1, 40(sp)
        sd      s2, 32(sp)
        sd      s3, 24(sp)
        sd      s4, 16(sp)
        sd      s5, 8(sp)
	
	#----------------------------------------------------------
	# Map:
        # s0 = board
        # s1 = group
        # s2 = used bitmask
        # s3 = notused (~used)
        # s4 = change_made
        # s5 = loop index (group_index) or temporary
	#----------------------------------------------------------

	mv      s0, a0        # s0 <- board
        mv      s1, a1        # s1 <- group
        mv      s2, a2        # s2 <- used bitmask

        # s3 = notused = ~used
        not     s3, s2

        li      s4, 0         # change_made = 0
        li      s5, 0         # group_index = 0

loop_clear:
        li      t0, 9
        bge     s5, t0, done_clear   # if group_index >= 9: goto done

        # board_index = group[group_index]
        add     t1, s1, s5           # address = group + group_index
        lbu     t2, 0(t1)            # board_index = lbu(address)

        # element = board[board_index]
        slli    t3, t2, 1            # scaled_board_index = board_index * 2
        add     t4, s0, t3           # address of board[board_index]
        lh      t5, 0(t4)            # elt = board[board_index]

        # count = count_bits(elt)
        mv      a0, t5
        jal     count_bits           # returns bit count in a0
        mv      t6, a0              # t6 = count

        # if count != 1: attempt to clear bits
        li      t0, 1
        beq     t6, t0, skip_clear   # if count == 1: skip clear

        # new_elt = elt & notused
	add     t1, s1, s5           # address = group + group_index
        lbu     t2, 0(t1)            #
	slli    t3, t2, 1            #
	add     t4, s0, t3           #
	lh      t5, 0(t4)            # elt = board[board_index]
        and     a5, t5, s3

        # if new_elt != elt
        beq     a5, t5, skip_store

        # board[board_index] = new_elt
        sh      a5, 0(t4)
        li      t0, 1
        mv      s4, t0              # change_made = 1

skip_store:
skip_clear:
        addi    s5, s5, 1           # group_index++
        j       loop_clear

done_clear:
        # return change_made in a0
        mv      a0, s4

        # Epilogue:
        ld      ra, 56(sp)
        ld      s0, 48(sp)
        ld      s1, 40(sp)
        ld      s2, 32(sp)
        ld      s3, 24(sp)
        ld      s4, 16(sp)
        ld      s5, 8(sp)
        addi    sp, sp, 64
        ret


# ------------------------------------------------------------------------------
# pencil_marks(board, table) -> 0 or 1
#
#   changed = 0
#   for group_start = 0; group_start < 27*9; group_start += 9:
#       used = get_used(board, table + group_start)
#       delta = clear_used(board, table + group_start, used)
#       if (delta != 0):
#           changed = 1
#   return changed
# ------------------------------------------------------------------------------
pencil_marks:
	#P rologue:
	addi	sp, sp, -48
	sd      ra, 40(sp)
        sd      s0, 32(sp)
        sd      s1, 24(sp)
        sd      s2, 16(sp)
        sd      s3, 8(sp)

	#----------------------------------------------------------
	# Map:
	# s0 = board
	# s1 = table
	# s2 = group_start
	# s3 = changed
	# t0 = compare_value
	#----------------------------------------------------------

	mv	s0, a0		# s0 = board
	mv	s1, a1		# s1 = table
	li	s2, 0		# group_start = 0
	li	s3, 0		# changed = 0
	
loop_pencil:
	
	li	t0, 243		# compare_value = 243
	bge	s2, t0, done_pencil	# if group_start >= 243: goto done
	
	# used = get_used(board, table+group_start)
	add	t1, s1, s2	# address = table + group_start
	mv	a0, s0		# a0 = board
	mv	a1, t1		# a1 = table + group_start
	jal	get_used	# returns 'used' in a0
	mv	t2, a0		# t2 = used
	
	# delta = clear_used(board,table+group_start, used)
	add	t1, s1, s2	# address = table + group_start
	mv	a0, s0		# a0 = board
	mv	a1, t1		# a1 = table + group_start
	mv	a2, t2		# a2 = used
	jal	clear_used	# returns 'delta' in a0
	mv	t3, a0		# t3 = 'delta'

	# if delta != 0: changed = 1
	beqz	t3, skip_set
	li	s3, 1

skip_set:
	#group_start +=9
	li	t5, 9
	add	s2, s2, t5
	j	loop_pencil

done_pencil:	
	mv	a0, s3		# return changed as a0

	# Epilogue
	ld	ra, 40(sp)
	ld	s0, 32(sp)
	ld	s1, 24(sp)
	ld	s2, 16(sp)
	ld	s3, 8(sp)
	addi	sp, sp, 48	
	ret
