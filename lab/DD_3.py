from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np


def zvezda1(beta, R=3):
    alpha = np.arange(0, 2*np.pi, 0.1)
    x =  R*np.cos(alpha)**3
    y =  R*np.sin(alpha)**3

    beta= np.deg2rad(beta)
    X =  x * np.cos(beta) - y * np.sin(beta)
    Y =  x * np.sin(beta) + y * np.cos(beta)
    return X, Y


fig, ax = plt.subplots()
zvezda, = plt.plot([], [], '-', color='r', label='Ball')


def animate(beta):
    zvezda.set_data(zvezda1(beta))
    return zvezda


edge = 3
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

ani = FuncAnimation(fig, animate, frames=100, interval=30)
ani.save('zvezda.gif', writer="pillow")