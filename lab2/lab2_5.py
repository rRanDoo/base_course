a=int(input('Введите число 1: '))
b=int(input('Введите число 2: '))
if b==0:
    print('деление на ноль :(')
elif a%b==0:
    print('Делиться')
    print('Частное',a//b)
else:
    print('Не делиться')
    print('Остаток',a%b)
    print('Частное',a//b)