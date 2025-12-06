import numpy as np
N = int(input("Введите количество строк N: "))
M = int(input("Введите количество столбцов M: "))
i, j = np.indices((N, M))
mememe = np.sin(N * i+ M * j + 1)
mememe[mememe < 0] = 0
print("Результат:")
print(np.array2string(mememe, formatter={'float_kind': lambda x: "%.4f" % x}))