# https://stepik.org/lesson/294243/step/15?unit=275922
n = int(input())                # получаем кол-во циклов
num1 = 0                        # число 1
num2 = 1                        # число 2
for i  in range(n):             # цикл до N
    num2 = num1 + num2          # присваиваем переменной num2 новое значение суммы этой переменной с предыдущей
    num1 = num2 - num1          # переменной num1 присваиваем значение которое было в num2
    print(num1,end=' ')