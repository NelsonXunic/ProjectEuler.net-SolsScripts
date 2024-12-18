# This is a script used to solve a problem from the bank of problems found in ProjectEuler.net
# https://projecteuler.net/archives
# Problem 3: Largest Prime Factor
# The problem is as follows:
# The prime factors of 13195 are 5, 7, 13, and 29.
# What is the largest prime factor of the number 600851475143?

def largest_prime_factor(n):
    i = 2
    while i * i < n:
        while n % i == 0:
            n = n // i
        i += 1
    return n

if __name__ == '__main__':
    print(largest_prime_factor(600851475143))