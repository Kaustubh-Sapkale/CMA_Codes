import matplotlib.pyplot as plt
import numpy
from scipy.integrate import solve_ivp


def solve(x0, v0, mu, t0, T, n):
    def vdp_derivatives(_ , y):
        x, v = y
        return [v, mu * (1 - x * x) * v - x]

    t = numpy.linspace(t0, T, n)

    sol = solve_ivp(fun=vdp_derivatives, t_span=[t0, T], y0=[x0, v0], t_eval=t ) 


    y_points = sol.y[0]

    i1 = 0
    for i in range(n - 1, 0, -1):
        if y_points[i] <= 0 and y_points[i - 1] >= 0:
            i1 = i
            break

    i2 = -1
    for i in range(i1 - 1, 0, -1):
        if y_points[i] <= 0 and y_points[i - 1] >= 0:
            i2 = i
            break

    timePeriod = abs(t[i1] - t[i2])
    print(f"The period of the limit cycle is approximately {timePeriod:.3f} for {mu}")

    plt.title(f"Van der Pol equation for {mu}")
    plt.xlabel("t")
    plt.ylabel("x(t)")
    plt.plot(t, y_points)
    plt.grid()
    plt.show()


if __name__ == "__main__":
    mu = 0
    solve(0, 10, 0, mu, 200, 10000)
