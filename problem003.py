'''
Project Euler: Problem 3: Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the given number?
'''

def largestPrimeFactor(n):
    largestPrime = -1
    i = 2
    while i <= n:
        while n%i == 0:
            largestPrime = i
            n = n/i
        i += 1
    return largestPrime

print (largestPrimeFactor(600851475143))
