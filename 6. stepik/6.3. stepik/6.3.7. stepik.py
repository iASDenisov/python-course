# https://stepik.org/lesson/265110/step/7?unit=246058

from math import*

a,b,c = float(input()),float(input()),float(input())
D = b ** 2 - (4 * a * c) # нахождение дискриминанта
if D>0:
    x1 = (-b + sqrt(b ** 2 - (4 * a *c)))/ (2 * a)
    x2 = (-b - sqrt(b ** 2 - (4 * a *c)))/ (2 * a)
    if x1 > x2:
        print(x2,x1,sep='\n')
    else:
        print(x1,x2,sep='\n')
elif D == 0:
    print(-b / (2 * a))
else:
    print('Нет корней')