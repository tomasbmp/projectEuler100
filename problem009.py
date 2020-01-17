'''
Project Euler: Problem 9: Special Pythagorean triplet

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc such that a + b + c = n.
'''
import math

def specialPythagoreanTriplet(n):
    for c in range(math.ceil(n/3), math.floor(n/2)+1):
        # Using that a+b+c=n and a^2+b^2=c^2 we can write b as n-c-a and
        # expand the second equation, which will lead us to a quadratic
        # equation with only one variable (a), and we know how to solve that.
        # k2*a^2 + k1*a + k0 = 0
        k2 = 2
        k1 = -2*(n-c)
        k0 = (n*n - 2*c*n)
        delta = k1*k1 - 4*k2*k0
        if delta >= 0:
            a1 = (-1*k1 + math.sqrt(delta))/(2*k2)
            a2 = (-1*k1 - math.sqrt(delta))/(2*k2)
            b1 = n-c-a1
            b2 = n-c-a2
            if a1>=0 and a1.is_integer() and a1!=b1 and a1!=c and b1!=c:
                return int(a1*b1*c)
            if a2>=0 and a2.is_integer() and a2!=b2 and a2!=c and b2!=c:
                return int(a2*b2*c)
    return -1

print(specialPythagoreanTriplet(1000))
