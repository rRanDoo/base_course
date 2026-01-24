import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

def circle_move(R, t):
    x = np.sin(t)*(np.exp(np.cos(t))-2*np.cos(4*t)+ np.sin**5(t/12))
    y = np.cos(t)*(np.exp(np.cos(t))-2*np.cos(4*t)+ np.sin**5(t/12))
    return x, y


fig, ax = plt.subplots()
ball, = plt.plot([], [], 'o', color='r', label='Ball')
ball_line, = plt.plot([], [], '-', color='r', label='Ball')

coords = np.zeros((180, 2))


def animate(i):
    coords[i] = circle_move(R=2, angle_vel=1, time=i)
    ball.set_data([coords[i][0]], [coords[i][1]])
    ball_line.set_data(coords[:i, 0], coords[:i, 1])
    return ball, ball_line


edge = 3
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

ani = FuncAnimation (fig, animate, frames=180, interval=30)
ani.save('ani.gif', writer="pillow")