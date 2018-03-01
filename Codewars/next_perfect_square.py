# link to challenge: https://www.codewars.com/kata/find-the-next-perfect-square/train/

"""
Problem Statement:

You might know some pretty large perfect squares. But what about the NEXT one?
Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. 
Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.
If the parameter is itself not a perfect square, than -1 should be returned. You may assume the parameter is positive.
"""

# Return the next square if sq is a square, -1 otherwise
def find_next_square(sq):
    # find square root
    temp = sq ** 0.5
    # check if argument passed is a perfect square,
    # that is, it should be divisible by its square root without a remainder
    if (temp - int(temp)) > 0:
        return -1
    else:
        temp += 1
        return temp * temp
