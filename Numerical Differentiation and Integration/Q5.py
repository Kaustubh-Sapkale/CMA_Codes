
from math import exp
from scipy import integrate
from numpy import linspace
import numpy as np
import matplotlib.pyplot as plt


def fun(x):
    return 2 * x * exp(x * x)


def integral(x):
    return exp(x * x)


def visualize():

    u_min = 0
    u_max = 0.2
    numPoints = 1000

    upts = linspace(u_min, u_max, numPoints+1)  
    upts = list(upts)
    upts.remove(0)
    upts = np.array(upts)
    actual_area = []  
    trapezoidal = []
    quadrature = [] 
    simpson = [] 
    romberg = []

    for u in upts:
        x_axis = linspace(u_min, u, numPoints) 
        y_axis = [fun(x) for x in x_axis] 
        actual_area.append(integral(u) - integral(u_min)) 
        trapezoidal.append(integrate.trapezoid(y_axis, x_axis)) 
        quadrature.append(integrate.quad(fun, u_min, u)[0]) 
        simpson.append(integrate.simpson(y_axis, x_axis)) 
        romberg.append(integrate.romberg(fun, u_min, u)) 

    plt.title(f"Visualizing various integration functions in scipy.integrate module\n")
    plt.xlabel("u")
    plt.ylabel("area")


    plt.plot(upts, actual_area, c="r", label="Actaul Area")

    plt.plot(upts, trapezoidal, c="b", label="Trapezoidal")

    plt.plot(upts, quadrature, c="g", label="General purpose")

    plt.plot(upts, simpson, c="y", label="Simpson")


    plt.plot(upts, romberg, c="brown", label="Romberg")

    plt.grid()
    plt.legend(loc="upper left")
    plt.show()


if __name__ == "__main__":
    visualize( )
