                .global gcd
                .text

gcd:
	# a0 holds a on entry
	# a1 holds b on entry
	mv t0, a0	# t0 = a
	mv t1, a1	# t1 = b

loop_start:
	bne t0, t1, if_block	# jump to if_block if a != b
	mv a0, t0		# a0 = a  ( to return a)
	j end			# loop breaks if a = b, jump to end

if_block:
	blt t0, t1, else_block	# jump to else_block if a (t0) is less than b (t1)
	sub t0, t0, t1		# a = a - b
	j loop_start		# jump back to start of loop

else_block:
	sub t1, t1, t0
	j loop_start

end:
	jr ra



# Euclid's algorithm
# ==================
#
# Euclid's algorithm computes the greatest common divisor between two
# integers. For simplicity we will only consider positive numbers. You
# will implement rv64 code to mimic the following:
# ```
# def gcd(a, b):
#     while a != b:
#         if a > b:
#             a = a - b
#         else:
#             b = b - a
#     return a
