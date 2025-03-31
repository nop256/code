                .global fibonacci
                .text

fibonacci:			# def fibonacci(n):
	# Arguments:
	# a0 = n  --  (number)
	# Returns:
	# a0	
	
	# Initialize variables
	li t0, 0		# t0 = a, a = 0
	li t1, 1		# t1 = b, b = 1
	li t2, 0		# t2 = i, i = 0 at start of loop :: initializes loop
	mv t3, a0		# a0(argument) = n, t3 = n
	# Initialize loop
loop:
	bge t2, t3, done	# stop loop if i == n
	add t4, t0, t1		# temp = a + b
	mv t0, t1		# a = b
	mv t1, t4		# b = temp	
	addi t2, t2, 1		# i += 1

	j loop			# jump back to loop start, repeat until i == n
	
done:
	mv a0, t0		# saving t0(a) to a0 (return value register 0)

	jr ra			# return a0(a) -- copied from t0 on line 26

		
		
		
		
		
		
		
		
		
		
		
		
# Fibonacci numbers
# =================
#
# Write an assembly language function to compute numbers in the
# Fibonacci sequence. The function will take a single parameter and
# return a single result. You should write your code to closely mimic
# the following pseudocode:
#
# ```
# def fibonacci(n):
#     a = 0
#     b = 1
#     for i in range(n):
#         temp = a + b
#         a = b
#         b = temp
#     return a
# ```
