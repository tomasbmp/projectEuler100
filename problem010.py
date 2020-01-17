'''
Project Euler: Problem 10: Summation of primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below n.
'''

def primeSummation(n):
    if n < 1: return -1
    if n <= 2: return 0
    primes = [2]
    candidate = 3
    summation = 2
    while candidate < n:
        still_prime = True
        for prime in primes:
            if candidate%prime == 0:
                still_prime = False
                break
        if still_prime:
            primes.append(candidate)
            summation += candidate
        candidate += 2
    return summation

print(primeSummation(2000000))
