import matplotlib.pyplot as plt 
import numpy as np
import math

def fun(x):
    return math.sin(x**2)

def derivative(x):
    return math.cos(x**2) * 2 * x

def FinitDifferenceApp(x , h = 0.01 , type = 'f'):
    if type == 'f':
        return (fun(x+h) - fun(x)) / h
    elif type == 'b':
        return (fun(x) - fun(x-h)) / h
    elif type == 'c':
        return (fun(x+h) - fun(x-h)) / (2 * h)

def visualise():
    x_axis = np.linspace(0,1,100)
    ffd = [abs(FinitDifferenceApp(i , type='f')  - derivative(i)) for i in x_axis]
    bfd = [abs(FinitDifferenceApp(i , type='b')  - derivative(i)) for i in x_axis]
    cfd = [abs(FinitDifferenceApp(i , type='c')  - derivative(i)) for i in x_axis]

    
    #plotting
    plt.plot(x_axis ,  ffd , color = 'r' , label = "Forward Finit Difference")
    plt.plot(x_axis , bfd , color = 'g' , label = "Backword Finit Difference")
    plt.plot(x_axis , cfd , color = 'm' , label = "Center Finit Defference")
    plt.title("Visualise Actual derivative and Forward Finit Difference")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(linestyle = '--')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    visualise()


