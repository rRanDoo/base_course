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


def astroida(R, t):
      t = np.arange(0, 18*np.pi, 0.01)
      R=16
      x = R * np.cos(t)**3
      y =  R * np.sin(t)**3
      plt.plot(x, y, ls='-', lw=3)
      plt.axis('equal')
      plt.savefig('me.png') 
astroida(16, 1)