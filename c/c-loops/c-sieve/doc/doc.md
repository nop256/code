The Sieve of Eratosthenes
-------------------------

The sieve of Eratosthenes is an algorithm for finding all prime
numbers up to a fixed limit. See this Wikipedia articles for more
details and an animated demo of how it works:

* <https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes>

Write a function called `sieve` in `sieve.c` that matches the
prototype given in `main.c`. Your code should implement the sieve:

*   You will be given an array of bool values (passed in as a
    pointer) and the size of that array.
*   Initialize all elements of the array to true: you will start by
    assuming every number is prime (true) and then cross off values
    (mark as false) that prove to be non-prime.
*   You can ignore elements 0 and 1.

The basic approach is to scan the list starting at 2. By the time
you get to a number, the list will accurately name that number as
prime or non-prime.

*   The outer loop starts at 2 and counts up to size (it can
    actually stop at the square root of size--to test this, square
    your counter and compare that with size instead of using the
    counter itself).
*   If the number is non-prime, immediately skip to the next
    iteration of the loop.
*   For prime numbers, cross off (set to false) every multiple of
    that number up to size.

Note that you should not be using multiplication, division, or the
modulo (remainder) operator. The only exception is when testing if
the outer loop is finished (squaring the counter to compare it with
the size of the list).

This is a very efficient way to accomplish this task. Each non-prime
number may be crossed off multiple times, but only once for each
unique prime factor, and that tends to be a small number. In
particular, this is much more efficient than testing each number
in the range individually.

You do not need to print out any results or return anything. Since
you are modifying the array in place, `main` will be able to see the
results.

Take a few minutes to read through `main` to see how an array can be
allocated and freed.
