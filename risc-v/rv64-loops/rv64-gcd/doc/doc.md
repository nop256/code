Euclid's algorithm
==================

Euclid's algorithm computes the greatest common divisor between two
integers. For simplicity we will only consider positive numbers. You
will implement rv64 code to mimic the following:

```
def gcd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

For a full description of how it works, see the Wikipedia article:

* https://en.wikipedia.org/wiki/Euclidean_algorithm
