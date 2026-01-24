
import matplotlib.pyplot as plt
import numpy as np

def astroida(R, t):
      t = np.arange(0, 18*np.pi, 0.01)
      R=16
      x = R * np.cos(t)**3
      y =  R * np.sin(t)**3
      plt.plot(x, y, ls='-', lw=3)
      plt.axis('equal')
      plt.savefig('mуe.png') 
astroida(16, 1)