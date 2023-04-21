import math
from scipy.integrate import quad
import matplotlib.pyplot as plt
from numpy import linspace, linalg
from poly import Polynomial

import math

def fun(x):
    return math.e ** x

def FFT(n):
    if not isinstance(n , int):
        raise Exception("Invalid Input n should be int")
    if n < 0:
        raise Exception("Invalid Input n should be nonnegative")

    l , r = -math.pi , math.pi
    x_axis = linspace(l, r, 100)
    y_points1 = [fun(i) for i in x_axis]

    coefficients = []

    for k in range(0, n + 1):
        ak = (1 / math.pi) * quad(lambda x: fun(x) * math.cos(k * x), l, r)[0]
        bk = (1 / math.pi) * quad(lambda x: fun(x) * math.sin(k * x), l, r)[0]
        coefficients.append((ak, bk))
        print(f"a{k} = {ak}, b{k} = {bk}")

    
    
    y_points2 = []
    for x in x_axis:
        
        s1, s2 = 0, 0
        for k in range(1, n + 1):
            s1 += coefficients[k][0] * math.cos(k * x)
            s2 += coefficients[k][1] * math.sin(k * x)
        y_points2.append((coefficients[0][0] / 2) + s1 + s2)

    plt.title("FFT")
    plt.xlabel("x")
    plt.ylabel("y")

    plt.plot(x_axis, y_points1, "r", label="e^x")
    plt.plot(x_axis, y_points2, "b", label="Fourier Approximation")
    plt.grid()
    plt.legend()
    plt.show()

    

if __name__ == "__main__":
    print(FFT(5))