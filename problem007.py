'''
Project Euler: Problem 7: 10001st prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the nth prime number?

'''

def nthPrime(n):
    if n < 1: return -1
    primes = []
    candidate = 2
    while len(primes) < n:
        still_prime = True
        for prime in primes:
            if candidate%prime == 0:
                still_prime = False
                break
        if still_prime: primes.append(candidate)
        candidate += 1
    return primes[n-1]

print(nthPrime(10001))
