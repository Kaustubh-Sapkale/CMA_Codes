import numpy as np
import matplotlib.pyplot as plt
import math
from poly import Polynomial

def f(x):
    return -2*x 

def exact_fun(x):
    return 5 * math.exp(-2 * x)

def forward_euler(f, x0, x_inputs , step_size):
    n = len(x_inputs)
    x = [x0]
    for i in range(n-1):
        x.append(x[i] + step_size * f(x[i]))
    return x




if __name__ == "__main__":
    x0 = 5
    x_input = list(np.linspace(0, 10, 100))
    y_point = [exact_fun(i) for i in x_input]

    step_sizes = [0.1, 0.5, 1, 2, 3]
    for h in step_sizes:
        x_inputs = np.arange(0, 10+h, h)
        y_points = forward_euler(f, x0, x_inputs , h)
        plt.plot(x_inputs, y_points, label=f'step size {h}')

    plt.plot(x_input,y_point , label='exact solution')
    plt.title("forward Euler method to solve the ODE x'(t) = −2x(t)")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.xlim(0 , 10)
    plt.ylim(-5 , 5)
    plt.legend()
    plt.show()
