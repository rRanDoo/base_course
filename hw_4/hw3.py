import numpy as np


def parabola(a, b, N):
    x = np.linspace(a, b, N)
    return {'x': x}, {'y': x**2}


value = parabola(-1, 1, 10)
print(value[0])
print(value[1])