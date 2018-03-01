# link to challenge: https://projecteuler.net/problem=1

"""
Problem Statement:

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

def sum_of_multiples(x, y, z):
    sum = 0
    for num in range(x, z):
        if (num % x == 0) or (num % y == 0):
            sum += num
    print sum
    
sum_of_multiples(3, 5, 1000)   # Answer: 233168
