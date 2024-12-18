# This is a script used to solve a problem from the bank of problems found in ProjectEuler.net
# https://projecteuler.net/archives
# Problem 7: 10001st Prime
# The problem is as follows:
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

list_of_primes = [2, 3, 5, 7, 11, 13]
def is_prime(n):
    i = 0
    while list_of_primes[i]<=n//2:
        if n % list_of_primes[i] == 0:
            return False
        i += 1
    return True

def find_prime(n):
    i =17
    while len(list_of_primes) < n:
        if is_prime(i):
            list_of_primes.append(i)
        i += 2
    return list_of_primes[n-1]

if __name__ == '__main__':
    print(find_prime(10001))