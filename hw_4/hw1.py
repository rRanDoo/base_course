def energy(m,v,h,g):
    potential=m*g*h
    kinetic=(m*v**2)/2
    return kinetic+potential
e= energy(5,10,100,9.8)
print(e)