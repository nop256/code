


def convert_fahrenheit(Celsius):
    Fahrenheit = Celsius * 9 / 5 + 32
    return Fahrenheit

temps = [10,20,30]

for Celsius in temps:
    print(convert_fahrenheit(Celsius))
   





'''
32.5) For with Function

Create a function called `convert_fahrenheit` that consumes a single temperature
in Celsius and returns it converted to Fahrenheit. Then, call that function
inside of a `for` loop to convert and print each of the following temperatures:
`10`, `20`, and `30`. Make sure you write the for loop _outside_ of your
function.

You may want to refer to the last problem. Just be sure to read these
instructions carefully and notice the differences between the two problems -
write a function that consumes a SINGLE temperature, not a list!'''
