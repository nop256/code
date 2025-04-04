# Formatted Printing Help

# This finds the log base 2 of a number, x
# Do NOT take the log of zero!
def Format(x):
    if x!=0:
        x = math.log(x)/math.log(2)
    return x

# This prints a string, filling in variable name for %s.
name = "Jill"
print("hello %s." % (name))

# This does the same thing, but makes sure name is exactly 10 spaces wide
name = "Jill"
print("hello %10s." % (name))

# This prints two integers
i = 5
j = 15
print("%d" % (i))
print("%d" % (j))

# This prints two integers, making them take 2 spaces each
i = 5
j = 15
print("%2d" % (i))
print("%2d" % (j))

# This left pads with zeros
i = 5
j = 15
print("%02d" % (i))
print("%02d" % (j))

# This supresses the return until afterwards
i = 5
j = 15
print("%02d" % (i),end="")
print("%02d" % (j),end="")
print()

# This prints a float that will take 6 spaces, with 2 right of the decimal
# left padded with zeros
x = 13.12345
print("%06.2f" % (x))

# This prints a string left justified, instead of its default, right justified.
# It's in a field 9 wide, and suppresses the return.
name = "jill"
x = name.ljust(9," ")
print (x,end="")
