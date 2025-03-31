                .global am_or_fm

                .text
am_or_fm:			
	li t0, 535
	blt a0, t0, check_fm
	
	li t1, 1605
	bgt a0, t1, return_zero

	li a0, 1
	jr ra

check_fm:
	li t2, 88
	blt a0, t2, return_zero
	
	li t3, 108
	bgt a0, t3, return_zero

	li a0, 2
	jr ra

return_zero:
	li a0, 0
	jr ra





 
 
# ``` python
# def am_or_fm(freq):
#     if freq >= 535 and freq <= 1605:
#         return 1
#     if freq >= 88 and freq <= 108:
#         return 2
#     return 0
# ```
# 
# In other words, it takes a single argument and returns 1 if the
#argument is in the right range to be an AM station, or 2 if the
#arbument is in the right range to be an FM station. It returns 0 if
#the number is not in either range.
#
#Write your function in `am_or_fm.s`. Run `make` from the command
#line to test your function.
