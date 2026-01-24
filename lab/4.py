
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


C,D=0.3,0.33
x, y = [0.1], [0.1] 


def update(i):
    x.append(x[i-1]**2-y[i-1]**2+C) 
    y.append(2*x[i-1]*y[i-1]+D)
    
    
    anim_object.set_data(x, y)

    return anim_object

fig, ax = plt.subplots()


anim_object, = plt.plot([], [], 'o', lw=2)
ax.set_xlim(-1, 1) 
ax.set_ylim(-1, 1) 
plt.axis('equal')
ani = FuncAnimation(fig, update,frames=100, interval=50) 
                                

ani.save('ani.gif', writer="pillow")