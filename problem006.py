'''
Project Euler: Problem 6: Sum square difference
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first n natural numbers and the square of the sum.
'''

def sumSquareDifference(n):
    if n < 0: return -1
    sum = 0
    for i in range(n):
        sum += pow(i+1, 2)
    return int(pow(n*(n+1)/2, 2) - sum)

print (sumSquareDifference(100))
