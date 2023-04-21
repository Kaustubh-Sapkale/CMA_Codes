import math
from scipy.integrate import quad
import matplotlib.pyplot as plt
from numpy import linspace, linalg
from poly import Polynomial

def fun(x):
    return math.e ** x

def weight(x):
        return 1

def legendre_poly( n=0):

    if not isinstance(n , int):
        raise Exception("Invalid Input n should be int")
    if n < 0:
        raise Exception("Invalid Input n should be nonnegative")

    num = Polynomial([-1, 0, 1]) ** n
   

    for i in range(n):
        num = num.derivative()

    ans = num / (2**n * math.factorial(n))

    return ans



def lsapp(n):
    if n < 0:
        raise Exception("Expected  l non-negative integer")

    l , r = -1 , 1
    x_points = linspace(l, r, 100)
    y_points = [fun(i) for i in x_points]

    
    leg_poly = []
    for i in range(n + 1):
        leg_poly.append(legendre_poly(i))

    a_j = [] 
    for j in range(n + 1):
        cj = quad(lambda x: weight(x) * leg_poly[j][x] * leg_poly[j][x], l, r)[0]
        aj = (1 / cj) * quad(lambda x: weight(x) * leg_poly[j][x] * fun(x), l, r)[0]
        a_j.append(aj)

    ans = Polynomial([0])
    for i in range(n + 1):
        ans = ans + (a_j[i] * leg_poly[i])

    plt.title("least square approximation")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.plot(x_points, y_points, "r", label="actual function")
    ans.show(l, r, "computed")
    plt.grid()
    plt.legend()
    plt.show()

    return ans

if __name__ == "__main__":
    print(lsapp(3))