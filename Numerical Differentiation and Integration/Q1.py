import matplotlib.pyplot as plt 
import numpy as np
import math

def fun(x):
    return math.sin(x**2)

def derivative(x):
    return math.cos(x**2) * 2 * x

def ForwardFinitDifferenceApp(x , h = 0.01):
    return (fun(x+h) - fun(x)) / h

def visualise():
    x_axis = np.linspace(0,1,100)
    der = [derivative(i) for i in x_axis]
    ffd = [ForwardFinitDifferenceApp(i) for i in x_axis]


    #plotting
    plt.plot(x_axis , der , color = 'b' , label = "derivative") 
    plt.plot(x_axis ,  ffd , color = 'r' , label = "Forward Finit Difference")
    plt.title("Visualise Actual derivative and Forward Finit Difference")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(linestyle = '--')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    visualise()


