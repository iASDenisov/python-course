'''
https://stepik.org/lesson/265083/step/14?unit=246031
'''
r1, c1, r2, c2 = int(input()), int(input()), int(input()), int(input())

# если строка откуда куда равны r1 == r2
# или столбец откуда куда равны c1 == c2
if r1 == r2 or c1 == c2:
    print('YES')
else:
    print('NO')
