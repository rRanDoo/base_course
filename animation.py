import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Создание пространства и подпространства для анимации
fig, ax = plt.subplots()

# Объект анимации
anim_object, = plt.plot([], [], '-', lw=2)

x, y = [], [] # Координаты объекта анимации
frames_interval = np.linspace(-100, 100, 100)

ax.set_xlim(-100, 100) # Пределы изменения переменной Х
ax.set_ylim(-1000, 1000) # Пределы изменения переменной У

# Функция подстановки параметра в объект анимации
def update(frame):
    x.append(frame) # Расчет координаты Х
    y.append((frame)**2) # Расчет координаты У
    
    # Передача координат объекту анимации
    anim_object.set_data(x, y)

    return anim_object


ani = FuncAnimation(fig, # Вызов пространства для анимации
                    update, # Вызов функции подстановки координат
                    frames=frames_interval, # Интервал значений
                    interval=45) # Интервал между кадрами,
                                 # по умолчанию 200 милисекунд

ani.save('animation_1.gif', writer="pillow")
