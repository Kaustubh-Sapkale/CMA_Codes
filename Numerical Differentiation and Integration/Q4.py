from math import exp
import matplotlib.pyplot as plt


def fun(x):
    return 2 * x * exp(x * x)


def fun_integral(x):
    return exp(x * x)


def visualize(a, b):
    numIntervals = 100 
    x_axis = [] 
    y_axis = []  

    actual_area = fun_integral(b) - fun_integral(a) 

  
    for M in range(1, numIntervals + 1):
        x_axis.append(M)
        
        H = (b - a) / M
        area = ((b - a) * (fun(a) + fun(b))) / (2 * M)
        for k in range(1, M):
            xk = a + (k * H)
            area += (b - a) * fun(xk) / M

        y_axis.append(area)

    plt.title(f"isualize, as a function of M (number of intervals), area under the curve")
    
    plt.plot(x_axis, y_axis, c="r", label="Approximate Area")
    plt.axhline(y=actual_area, color="b", label="Exact Area")
    plt.xlabel("M")
    plt.ylabel("area")
    plt.grid()
    plt.legend(loc="upper right")
    plt.show()


if __name__ == "__main__":
    visualize(1, 3)
