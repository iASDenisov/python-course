"""
Напишите программу, которая считывает три строки по очереди, а затем выводит их в обратной последовательности, каждую на отдельной строчке.

Формат входных данных
На вход программе подается три строки, каждая на отдельной строке.

Формат выходных данных
Программа должна вывести введенные строки в обратной последовательности, каждую на отдельной строке.
"""
a, b, c = input(), input(), input()
print(c,b,a, sep="\n")