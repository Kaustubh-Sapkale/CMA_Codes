
from scipy import interpolate as ip
import matplotlib.pyplot as plt
import math
import numpy as np
from matplotlib.animation import FuncAnimation


def true_fun(x):
    return math.tan(x) * math.sin(30 * x) * math.e ** x

# Create class to store data for each plot to be animated
class Anim:
    def __init__(self, ax, x_axis=np.linspace(0, 1, 200)):
        self.x = x_axis
        self.ax = ax

        # Define lines for each interpolation to be plotted
        self.line, = ax.plot([], [], 'k-', color='r', label="cubic_spline")
        self.line2, = ax.plot([], [], 'k-', color='g', label="Akima")
        self.line3, = ax.plot([], [], 'k-', color='m', label="Barycentric")

    def __call__(self, i):
        if i == 0:
            self.line.set_data([], [])
            return self.line

        # Define x and y axis data for each interpolation method
        x_axis = np.linspace(0, 1, 200)
        y_axis = []
        y_axis2 = []

        # Set limits for x and y axis
        self.ax.set_xlim(0, 1)
        self.ax.set_ylim(-4, 4)

        # Define points known for the current iteration
        self.x = np.linspace(0, 1, i)
        points_known = []
        for j in self.x:
            points_known.append(math.tan(j) * math.sin(30 * j) * math.e ** j)

        # Interpolate using BarycentricInterpolator
        if i > 1:
            bary_fun = ip.BarycentricInterpolator(self.x, np.array(points_known))
            y_axis = bary_fun(x_axis)

            # Interpolate using Akima1DInterpolator
            akima_fun = ip.Akima1DInterpolator(self.x, np.array(points_known))
            y_axis2 = akima_fun(x_axis)

            # Interpolate using CubicSpline
            spline_fun = ip.CubicSpline(self.x, np.array(points_known))
            y_axis3 = spline_fun(x_axis)

            # Set data for each interpolation line
            self.line.set_data(x_axis, np.array(y_axis3))
            self.line2.set_data(x_axis, np.array(y_axis2))
            self.line3.set_data(x_axis, np.array(y_axis))

            # Set plot title
            plt.title(f"Different Interpolations of tan(x). sin(30x) .  e ^ x for {i} samples")
            return self.line, self.line2, self.line3


if __name__ == "__main__":
    # Create plot figure and axes
    fig = plt.figure(figsize=(6, 4))
    ax = fig.add_axes([0.1, 0.1, 0.85, 0.85])

    # Create instance of Anim class and run animation using FuncAnimation
    ftp = Anim(ax)
    anim = FuncAnimation(fig, ftp, frames=60, interval=500, save_count=10000)

    # Generate x and y data for true function and plot
    x_axis = np.linspace(0, 1, 200)
    y_axis = []
    for i in x_axis:
        y_axis.append(true_fun(i))



    fig = plt.plot(x_axis , y_axis , color = 'b' , label= "True")
    plt.ylim(-4 , 4)
    plt.xlim(0 , 1)
    plt.ylabel("f(x)")
    plt.xlabel("x")
    plt.grid(True)
    plt.legend(loc = "upper left")
    plt.title(f"Different Interpolations of tan(x). sin(30x) .  e ^ x for 0 samples")

    plt.show()


