import numpy as np
import time
x0=int(input("x0"))
y0=int(input("y0"))
v0x=int(input("v0x"))
v0y=int(input("v0y"))
g=9.8
t=0
sss=[]
for t in range(0,5,1):
    x=x0+v0x*t
    y=y0+v0y-(g*t**2)/2
sss.append([t,x,y])
print(sss)
step = 1
t=np.arange(0,5,step)
x=x0+v0x*t
y=y0+v0y-(g*t**2)/2
sss= np.zeros((len(t),3))
sss[:,0]=t
sss[:,1]=x
sss[:,2]=y
print(sss)