import math
from scipy.integrate import quad
import matplotlib.pyplot as plt
from numpy import linspace, linalg
from poly import Polynomial


def fun(x):
    return math.e ** x

def weight(x):
    return 1 / math.sqrt(1 - x**2)

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

def ortho(n):
    if n < 0:
        raise Exception("Invalid Input. nonnegative n is expected")

    l , r = -1 , 1

    cpolys = []  
    for i in range(n):
        cpolys.append(chebyshev(i))


    mat = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            integrand = lambda x: weight(x) * cpolys[i][x] * cpolys[j][x]
            row.append(quad(integrand, l, r)[0])

        mat.append(Polynomial(row))

    for i in mat:
        print(i)

if __name__ == "__main__":
    ortho(5)