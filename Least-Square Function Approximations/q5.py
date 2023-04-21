import math
from scipy.integrate import quad
import matplotlib.pyplot as plt
from numpy import linspace, linalg
from poly import Polynomial


def fun(x):
    return math.e ** x

def chebyshev(n):
    if not isinstance(n , int):
        raise Exception("Invalid Input n should be int")
    if n < 0:
        raise Exception("Invalid Input n should be nonnegative")


    a = Polynomial([1])
    a_1 = Polynomial([0, 1])

    if n == 0:
        return a
    elif n == 1:
        return a_1
    for _ in range(2, n + 1):
        a_n = 2 * a_1 * Polynomial([0, 1]) - a
        a = a_1
        a_1 = a_n
    ans = a_1
    return ans


if __name__ == "__main__":
    print(chebyshev(0))
    print(chebyshev(1))
    print(chebyshev(2))
    print(chebyshev(3))