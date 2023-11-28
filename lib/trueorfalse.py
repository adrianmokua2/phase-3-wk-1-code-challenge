#!/usr/bin/env python3
def two_positive_numbers(a, b, c):
    # the if and elif statement should return True if exactly two of the three integers are positive numbers (greater than zero)
    if a > 0 and b > 0 and c <= 0:
        return True
    elif a > 0 and b <= 0 and c > 0:
        return True
    elif a <= 0 and b > 0 and c > 0:
        return True
    # otherwise, the function should return False
    else:
        return False
print(two_positive_numbers(7,8,9))    