# https://stepik.org/lesson/313439/step/6?unit=295959
# декодирование шифра Цезаря

n,s = int(input()), str(input())
i = 0
dt = 26
while i != len(s):
    s1 = ord(s[i]) - n
    if s1 < 97:
        s1 += dt
    print(chr(s1),end='')
    i+=1