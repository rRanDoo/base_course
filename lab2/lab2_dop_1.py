print('a*(x**2)+b*x+c=0:')
a=int(input('Введите коэффицент a: '))
b=int(input('Введите коэффицент b: '))
c=int(input('Введите коэффицент c: '))
D= (b**2)-4*a*c
if D>0:
    x1=((-b)+D**0.5)/(2*a)
    x2=((-b)-D**0.5)/(2*a)
    print(x1,x2)
elif D==0:
    x=(-b)/(2*a)
    print(x)
else:
    print('Корней нет')