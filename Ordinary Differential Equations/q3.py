
import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def ode(theta, v, g, L):
    return (v, -(g / L) * math.sin(theta))

def cords(th , L):
    return L * math.sin(th), -L * math.cos(th)

def solve( theta0, v0, h, t0, T, g, L):

    t = t0
    theta = theta0
    v = v0
    list_theta = [theta0]  

    while t <= T:
        x , y = ode(theta, v, g, L)
        theta = theta + h * x
        v = v + h * y
        list_theta.append(theta)
        t += h

    

    fig = plt.figure()
    ax = fig.add_subplot(aspect="equal")

    x0, y0 = cords(theta0 , L)
    (line,) = ax.plot([0, x0], [0, y0], lw=1, c="k")

    bob_radius = 0.004
    bob = ax.add_patch(plt.Circle(cords(theta0 , L), bob_radius, fc="b", zorder=1))

    patches = [line, bob]

    def init():
        ax.set_title("Simple Gravity Pendulum")

        ax.set_xlim(-L * 1.5, L * 1.5)
        ax.set_ylim(-L * 1.5, L * 1.5)

        return patches

    def animate(i):

        x, y = cords(list_theta[i] , L)
        line.set_data([0, x], [0, y])
        bob.set_center((x, y))


        return patches

    anim = FuncAnimation(fig,animate,init_func=init,frames=100000,repeat=True,interval=1,blit=True,)
    plt.show()


if __name__ == "__main__":
    solve(math.pi / 4, 0,0.001, 0, 10, 10, 0.1)

