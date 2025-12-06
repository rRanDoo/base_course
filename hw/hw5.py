import hw4
import numpy as np
col1 = int(input(f"Введите индекс первого столбца (0-{hw4.M-1}): "))
col2 = int(input(f"Введите индекс второго столбца (0-{hw4.M-1}): "))
if col1 < 0 or col1 >= hw4.M or col2 < 0 or col2 >= hw4.M:
    print("Ошибка: индексы столбцов выходят за границы массива")
else:
    hw4.mememe[:, [col1, col2]] = hw4.mememe[:, [col2, col1]]
    print(f"Массив после замены столбцов {col1} и {col2}:")
    print(np.array2string(hw4.mememe, formatter={'float_kind': lambda x: f"{x:.4f}"}))