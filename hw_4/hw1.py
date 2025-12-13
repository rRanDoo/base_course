def energy(m, v, h, g):
    kinetic = m * v**2 / 2
    potential = m * g * h
    return kinetic + potential


E = energy(5, 10, 100, 9.8)
print(E)


def energy(m, v, h, g=9.8):
    kinetic = m * v**2 / 2
    potential = m * g * h
    return kinetic + potential


E = energy(5, 10, 100)
print(E)


def energy(m=0, v=0, h=0, g=9.8):
    kinetic = m * v**2 / 2
    potential = m * g * h
    return kinetic + potential


E = energy()
print(E)


def energy(g=9.8, **data):
    kinetic = data['m'] * data['v']**2 / 2
    potential = data['m'] * g * data['h']
    return kinetic + potential


E = energy(10, m=5, v=4, h=100)
print(E)

