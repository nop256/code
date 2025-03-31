                .global thermostat

                .text
thermostat:			#def thermostat(temp):
	li t0, 68
	blt a0, t0, start_heater
	
	li t1, 75
	bgt a0, t1, start_ac
	
	li a0, 0
	jr ra

start_heater:
	li a0, 1
	jr ra

start_ac:
	li a0, -1
	jr ra









#A thermostat monitors the current temperature and turns on the
#heater or air conditioner where the temperature is outside the
#desired range.

#Write a function that simulates a thermostat. It takes the current
#temperature as its only argument and does the following:

#*   If the temperature is below 68, return 1 to start the heater
#*   If the temperature is above 75, return -1 to start the AC
#*   In every other case, return 0

#Write your function in `thermostat.s`
