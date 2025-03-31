                .global count_jumps
                .text







#------------------------------------------------------------------------------
# Pseudocode
# def count_jumps(array:int, size: int):
#    count = 0
#    index = size-1
#    while 0 <= index < size:
#        next_index = index + array[index]
#        count += 1
#        if next_index < 0 or next_index >= size:
#            break
#        index = next_index
#    return count
#------------------------------------------------------------------------------

# int count_jumps(int *array, int size)
count_jumps:
	#-----------------------------------------------
	# Map
	# a0 = *array
	# a1 = size
	# t0 = index
	# t1 = next_index
	# t2 = count
	# t3 = constant 0
	# t4 = byte offset
	# t5 = array[index]
	#-----------------------------------------------
	
	li	t2, 0		# t2 = count = 0
	li	t3, 0		# t3 = 0 (for compares)
	addi	t0, a1, -1	# t0 = index = size-1

1:	blt	t0, t3, 2f	# if index < 0: return count
	bge	t0, a1, 2f	# if index >= size: return count
	
	slli	t4, t0, 3	# t4 = index * 8 (byte offset)
	add	t4, a0, t4	# t4 = base address + byte offset
	ld	t5, 0(t4)	# t5 = array[index]

	add	t1, t0, t5	# t1 = next_index = index + array[index]
	add	t2, t2, 1	# count += 1

	blt	t1, t3, 2f	# if next_index < 0: break and return count
	bge	t1, a1, 2f	# or next_index >= size: break and return count
	
	mv	t0, t1		# t0 = index = next_index
	j	1b		# repeat loop while 0<= index < size:
	
2:	mv	a0, t2		# return value = count
	jr	ra		# return count
