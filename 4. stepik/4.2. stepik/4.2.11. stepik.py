'''
https://stepik.org/lesson/265083/step/11?unit=246031
'''
a = int(input())
if (a % 7 == 0 or a % 17 == 0) and (a >= 1000 and a <= 9999):
    print('YES')
else:
    print('NO')