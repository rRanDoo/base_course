import numpy as np
import math
def vichisl_ploshad(shape, **kwargs):
    if shape == "круг":
       S = np.pi*kwargs['r']**2
    elif shape == "прямоугольник":
        S= kwargs['a']*kwargs['b']
    else:
        S=0.5*kwargs['a']*kwargs['h']
    return S
circle_area=vichisl_ploshad('круг', r=5)
print(circle_area)