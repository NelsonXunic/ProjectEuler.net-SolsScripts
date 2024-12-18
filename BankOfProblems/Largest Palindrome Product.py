# This is a script used to solve a problem from the bank of problems found in ProjectEuler.net
# https://projecteuler.net/archives
# Problem 4: Largest Palindrome Product
# The problem is as follows:
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def find_largest_palindrome():
    largest_palindrome = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            product = i * j
            if is_palindrome(product) and product > largest_palindrome:
                largest_palindrome = product
    return largest_palindrome

if __name__ == '__main__':
    print(find_largest_palindrome())

