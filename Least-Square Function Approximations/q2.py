import math
from scipy.integrate import quad
import matplotlib.pyplot as plt
from numpy import linspace, linalg
from poly import Polynomial

def fun(x):
    return math.sin(x) + math.cos(x)

def bestapprox(n):
    if not isinstance(n , int):
        raise Exception("Invalid Input n should be int")
    if n < 0:
        raise Exception("Invalid Input n should be nonnegative")
    #range 
    l ,r  = 0 , math.pi
    x_points = linspace(l , r , 100)
    y_points = [fun(i) for i in x_points]
    A = []

    #as per the equation given in the ppt computing matrix and vector
    #Ax = B
    
    for j in range(0, n + 1):
        row = []
        for k in range(0, n + 1):
            row.append(quad(lambda l: l ** (j + k), l, r)[0])
        A.append(row)
        
    b = []
    for j in range(0, n + 1):
        b.append(quad(lambda l: (l**j) * fun(l), l, r)[0])

    ans = Polynomial(list(linalg.solve(A, b)))
    ans.show(min(x_points) , max(x_points) , "approximation")
    plt.title("best approximation")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.plot(x_points , y_points , linestyle='dashed'  , linewidth = 2, color = 'r'  , label = "actual line")
    plt.grid()
    plt.legend()
    plt.show()
    return ans


if __name__ == "__main__":
    bestapprox(5)