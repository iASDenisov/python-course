# https://stepik.org/lesson/303083/step/14?unit=284990

s = input()
if s.count('f') == 1:
    print(s.find('f')) # вывод индекса вхождения
elif s.count('f') >= 2:
    print(s.find('f'), s.rfind('f')) # вывод индекса 1-го и последнего вхождения
else:
    print('NO')