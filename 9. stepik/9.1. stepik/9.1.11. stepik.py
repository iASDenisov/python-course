# https://stepik.org/lesson/284101/step/11?unit=265440

s = input()
for i in range(len(s)):
    if s[i] in '0123456789':
        print('Цифра')
        break
else:
    print('Цифр нет')   