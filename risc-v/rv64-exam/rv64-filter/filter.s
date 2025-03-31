                .global filter
                .text



#-------------------------------------------------------------------
# Pseudocode
#def filter(in_start, in_end, out_start):
#    while in_start < in_end:
#        # load the element from address in_start
#        elt = *in_start
#
#        # see if we should copy it
#        keep = check(elt)
#        if keep != 0:
#            # write the element to out
#            *out_start = elt
#
#            # increment out_start (this adds 8 to the address
#            # due to pointer arithmetic)
#            out_start += 1
#
#        # increment in_start (adds 8 to the pointer)
#        in_start += 1
#
#    # out_start is now the end of the output array
#    return out_start
#-------------------------------------------------------------------
# filter(src_start, src_end, out_start) -> out_end
filter:
	#-------------------------------------
	# Map
	# s0 = in_start
	# s1 = in_end
	# s2 = out_start
	# s3 = elt
	#-------------------------------------
	
	#-------------------------------------
	# Prelude
	addi 	sp, sp, -48
	sd	s0, 0(sp)
	sd	s1, 8(sp)
	sd	s2, 16(sp)
	sd	s3, 24(sp)
	sd	ra, 32(sp)
	#-------------------------------------
	
	mv	s0, a0	
	mv	s1, a1		# saving in_end to s1
	mv	s2, a2		# saving out_start to s2

1:	bge	s0, s1, 3f	# if in_start >= in_end: return out_start

	ld	s3, 0(s0)	# elt = *in_start
	#mv	s0, a0		# saving in_start pointer to s0
	mv	a0, s3		# output = elt : for check(elt)

	call	check		# check(elt) = a0

	beqz	a0, 2f		# check(elt) == 0: skip copy
	sd	s3, 0(s2)	# *out_start = elt
	addi	s2, s2, 8	# out_start += 1 (8 for byte offset of 64-bit system)

2:	addi	s0, s0, 8	# in_start += 1 (8 for byte offset of 64-bit system)	
	j	1b		# continue loop

3:	mv	a0, s2

	#-------------------------------------
	#Epilogue
	ld	s0, 0(sp)
	ld	s1, 8(sp)
	ld	s2, 16(sp)
	ld	s3, 24(sp)
	ld	ra, 32(sp)
	addi	sp, sp, 48
	#-------------------------------------

	jr	ra
