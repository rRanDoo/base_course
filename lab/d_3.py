import matplotlib.pyplot as plt
import numpy as np


R=3
alpha = np.arange(0, 2.5*np.pi,  0.1)  
x = R * np.cos(alpha)**3
y = R * np.sin(alpha)**3

beta= np.deg2rad0(30)
X = x0 + x * np.cos(alpha) - y * np.sin(alpha)
Y = y0 + y * np.cos(alpha) + x * np.sin(alpha)-3
plt.plot(x, y, ls='--', lw=3)
plt.axis('equal')
plt.xlim(-3,3)
plt.ylim(-3,3)
plt.savefig('fig_1.png')
