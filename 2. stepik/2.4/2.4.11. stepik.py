'''
Напишите программу, в которой вычисляется сумма, разность и произведение двух целых чисел,
введенных с клавиатуры.

Формат входных данных
На вход программе подаётся два целых числа, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести сумму, разность и произведение введённых чисел, каждое на отдельной строке.
'''
a,b = int(input()),int(input())
print(f'{a} + {b} = {a+b}\n{a} - {b} = {a-b}\n{a} * {b} = {a*b}')