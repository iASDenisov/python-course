# https://stepik.org/lesson/298796/step/2?unit=280623

num = int(input())

for i in range(1, num + 1):   # цикл отвечающий за количество рядов
    count = 0                 # счетчик для ряда, при каждом новом цикле обнуляется
    for j in range(i):        # 1й вложенный 
        count += 1            # увеличиваем цифру в ряду
        print(count, end='')  # вывод на печать без пробелов
    for k in range(i, 1, -1): # 2й вложенный 
        count -= 1            # уменьшаем цифру в ряду
        print(count, end='')  # вывод на печать без пробелов
    print()                   # переход на новую строку



