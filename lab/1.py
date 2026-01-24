import matplotlib.pyplot as plt
import numpy as np

def cikloida(R, t):
     t = np.arange(0, 18*np.pi, 0.01)
     R=3
     x = R * (t-np.sin(t))
     y = R * (1-np.cos(t))
     
     plt.plot(x, y, ls='-', lw=3)
     plt.axis('equal')
     plt.savefig('me.png')
cikloida(3,1)

