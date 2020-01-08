'''
Project Euler: Problem 5: Smallest multiple

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to n?
'''

def smallestMult(n):
    if n < 0: return -1
    if n == 0: return 0
    factors = [1]
    result = 1
    for i in range (2, n+1):
        for j in range(len(factors)):
            if i%factors[j] == 0:
                i /= factors[j]
                if i == 1: break
        if i > 1:
            factors.append(i)
            result *= int(i)
    return result

print(smallestMult(20))
