# link to challenge: https://www.codewars.com/kata/find-the-next-perfect-square/train/

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
