# 29.1) Renting Function

Create a function named `can_rent` that takes in two parameters: `age` and
`has_license`, in that order. Then, use your logic from codegrinder drill #27.2
as the function's body. The only difference in the logic here is that you should
now *return* strings instead of printing them. Call the function with your own
information (or make it up) and unit test it multiple times. Note that you will
need to get full test coverage - think of many different test cases so that your
unit tests try out every path through the code!

Here is the logic from #27.2:

```
if you are 21 or older
    if you are less than 1000 years old
        if you have a license
            then return "Can rent a car"
        otherwise
            then return "Doesn't have a license"
    otherwise
        then return "Too old"
otherwise
    then return "Too young"
```
