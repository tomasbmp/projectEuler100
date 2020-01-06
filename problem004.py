'''
Project Euler: Problem 4: Largest palindrome product

A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two n-digit numbers.
'''

def isPalindrome(n):
    # returns True if number is a palindrome
    # run time is O(len(n)) = O(log10(n))
    strn = str(n)
    for i in range(int(len(strn)/2)):
        if strn[i] != strn[-1*i-1]: return False
    return True

def largestPalindromeProduct(n):
    # naive solution
    largestPalindrome = 0    
    start = pow(10, n)-1
    stop = 0
    # stop means that once i reaches this number we know we've found our largest palindrome
    # e.g. n = 3, at one point we will find 906609 as a largest palindrome
    # 906609/999 = 907.5 so if the value of i reaches 907, we know we won't
    # be able to produce a number larger than 906609, so it must be our largest palindrome
    # this will reduce the number of iteractions from sum(1:999) = 499500 to sum(1:92) = 4278
    
    for i in range(start, 0, -1):
        if i <= stop: return largestPalindrome
        for j in range(start, i-1, -1):
            ij = i*j
            if ij > largestPalindrome and isPalindrome(ij):                                
                largestPalindrome = ij
                stop = ij/start

print(largestPalindromeProduct(3))
