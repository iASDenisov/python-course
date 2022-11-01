'''
https://stepik.org/lesson/284816/step/13?unit=266160
'''
num = int(input())
a = num % 10
b = (num % 100) // 10
c = num // 100     
print(f'Сумма цифр = {a+b+c}\nПроизведение цифр = {a*b*c}')
# [print(f'Сумма цифр = {a+b+c}\nПроизведение цифр = {a*b*c}') for a,b,c in [[int(i) for i in input()]]]