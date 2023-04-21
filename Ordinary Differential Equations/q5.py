from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp
def getnorm(r1, r2):
    return max(np.linalg.norm(r2 - r1), 10)

def double_derivative(r1, r2, r3):
    dd = list(((r2 - r1) / (getnorm(r2, r1) ** 3)) + ((r3 - r1) / (getnorm(r3, r1) ** 3)))
    return dd

def solve(init_r, init_v, t0, T, n):
   
    def vdp_derivatives( _ , y):
        r1x, r1y, r2x, r2y, r3x, r3y, v1x, v1y, v2x, v2y, v3x, v3y = y
        r1 = np.array([r1x, r1y])
        r2 = np.array([r2x, r2y])
        r3 = np.array([r3x, r3y])
        v1 = [v1x, v1y]
        v2 = [v2x, v2y]
        v3 = [v3x, v3y]
        v1d = double_derivative(r1, r2, r3)
        v2d = double_derivative(r2, r3, r1)
        v3d = double_derivative(r3, r1, r2)
        return v1 + v2 + v3 + v1d + v2d + v3d

    t = np.linspace(t0, T, n)

    sol = solve_ivp(fun=vdp_derivatives, t_span=[t0, T], y0=init_r + init_v, t_eval=t)


    r1x, r1y, r2x, r2y, r3x, r3y, *extra = sol.y


    fig = plt.figure()
    ax = fig.add_subplot(aspect="equal")

    bob_radius = 0.1
    body1 = ax.add_patch(plt.Circle((r1x[0], r1y[0]), bob_radius, fc="r", label="Body1"))
    body2 = ax.add_patch(plt.Circle((r2x[0], r2y[0]), bob_radius, fc="b", label="Body2"))
    body3 = ax.add_patch(plt.Circle((r3x[0], r3y[0]), bob_radius, fc="g", label="Body3"))

    patches = [body1, body2, body3]

    def init():

        ax.set_title("Three-Body Problem")
        ax.set_xlabel("X-axis")
        ax.set_ylabel("Y-axis")

        ax.set_xlim(-2, 6)
        ax.set_ylim(-4, 4)

        return patches

    def animate(i):
        body1.set_center((r1x[i], r1y[i]))
        body2.set_center((r2x[i], r2y[i]))
        body3.set_center((r3x[i], r3y[i]))
        return patches



    anim = FuncAnimation(fig,animate,init_func=init,frames=1000,interval=10,blit=True,)

    plt.legend()
    plt.show()

if __name__ == "__main__":
    r1 = [0, 0]
    r2 = [3, 1.73]
    r3 = [3, -1.73]
    v1 = [0, 0]
    v2 = [0, 0]
    v3 = [0, 0]
    solve(r1+r2+r3,v1+v2+v3, 0, 400, 1000)
