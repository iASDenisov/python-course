#  https://stepik.org/lesson/284101/step/14?unit=265440

s = input()
sogl,gl = 0, 0
for i in s:
    if i.lower() in 'ауоыиэяюёе':
        gl += 1
    elif i.lower() in 'бвгджзйклмнпрстфхцчшщ':
        sogl += 1
print(f'Количество гласных букв равно {gl}\nКоличество согласных букв равно {sogl}')