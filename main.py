# This is a script used to solve a problem from the bank of problem found in ProjectEuler.net
# https://projecteuler.net/archives
# Problem 1: Multiples of 3 and 5
# The problem is as follows:
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6, and 9.
# The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.

def sum_of_multiples(n):
    sum = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(sum_of_multiples(1000))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
