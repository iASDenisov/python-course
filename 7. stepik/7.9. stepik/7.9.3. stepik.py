# https://stepik.org/lesson/298796/step/3?unit=280623

a , b = int(input()), int(input())
total_maximum = 0                    # сумма делителей
digit = 0                            # число с максимальной суммой делителей

for i in range(a, b + 1):             # цикл перебирающий все числа от a до b включительно
    maximum = 0                       # обнуление суммы делителей, для нового цикла
    for j in range(1, i + 1):         # проверяем все числа от 1 до числа не превышающего проверяемое
        if i % j == 0:                # проверка на деление без остатка
            maximum += j              # суммируем делители
        if maximum >= total_maximum:  # если сумма делителей больше max суммы делителей
            total_maximum = maximum   # записываем в переменную максимальную
            digit = j
print(digit, total_maximum)           # вывод 