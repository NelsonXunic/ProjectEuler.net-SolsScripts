# This is a script used to solve a problem from the bank of problems found in ProjectEuler.net
# https://projecteuler.net/archives
# Problem 10: Summation of Primes
# The problem is as follows:
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

import os

# We create a list sieve where each index represents whether the number is prime.
# We mark 0 and 1 as non-prime. For each number starting from 2, if it is still marked as prime,
# we mark all its multiples as non-prime.
# Finally, we return the list of numbers that are still marked as prime.
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#:~:text=%5Bedit%5D-,Pseudocode,-%5Bedit%5D
def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for start in range(2, int(limit**0.5) + 1):
        if sieve[start]:
            for multiple in range(start*start, limit + 1, start):
                sieve[multiple] = False
    return [num for num, is_prime in enumerate(sieve) if is_prime]

def save_primes_to_file(primes, filename):
    with open(filename, 'w') as f:
        for prime in primes:
            f.write(f"{prime}\n")

def load_primes_from_file(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, 'r') as f:
        return [int(line.strip()) for line in f]

#
def find_prime_sum(limit, filename='primes.txt'):
    primes = load_primes_from_file(filename)
    if not primes or primes[-1] < limit:
        primes = sieve_of_eratosthenes(limit)
        save_primes_to_file(primes, filename)
    return sum(prime for prime in primes if prime < limit)

if __name__ == '__main__':
    print(find_prime_sum(2000000))
