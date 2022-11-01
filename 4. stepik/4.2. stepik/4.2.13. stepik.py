'''
https://stepik.org/lesson/265083/step/13?unit=246031
'''
# put your python code here
year = int(input())

# Делится на 4 без остатка но на 100 с остатком 
# или делится на 400 без остатка
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print('YES')
else:
    print('NO')
