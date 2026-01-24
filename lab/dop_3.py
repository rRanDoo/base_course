from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np

x0, y0 = 0, 0
t= np.linspace(0, 4*np.pi, 500)


x = 12*np.cos(t)+8*np.cos(1.5*t)
y = 12*np.sin(t)+8*np.sin(1.5*t)

fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-25, 25)
ax.set_ylim(-25, 25)
ax.set_aspect('equal')


line, = ax.plot([], [], 'r-', linewidth=2)
point, = ax.plot([], [], 'bo', markersize=8)

def init():
    line.set_data([], [])
    point.set_data([], [])
    return line, point

def animate(frame):
    alpha = frame * 0.05
    X = x0 + x * np.cos(alpha) - y * np.sin(alpha)
    Y = y0 + y * np.cos(alpha) + x * np.sin(alpha)

    line.set_data(X, Y)
    point.set_data([x0], [y0])
    return line, point

ani = FuncAnimation(fig, animate, frames=200, 
                    init_func=init, blit=True, interval=50)
ani.save('фф.gif', writer="pillow")