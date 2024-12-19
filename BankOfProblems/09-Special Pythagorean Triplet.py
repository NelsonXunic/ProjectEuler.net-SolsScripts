# This is a script used to solve a problem from the bank of problems found in ProjectEuler.net
# https://projecteuler.net/archives
# Problem 9: Special Pythagorean Triplet
# The problem is as follows:
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def find_pythagorean_triplet(n):
    for a in range(1, n):
        for b in range(a, n-a):
            c = n - a - b
            if a**2 + b**2 == c**2:
                return a * b * c

if __name__ == '__main__':
    print(find_pythagorean_triplet(1000))