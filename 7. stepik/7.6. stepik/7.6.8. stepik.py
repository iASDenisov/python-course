# https://stepik.org/lesson/298794/step/8?unit=280621

a = int(input())
n = 0
while  n != a:
    n += 1
    if (n > 4 and n <= 9) or (n > 16 and n <= 37) or (n > 77 and n <= 87):
        continue
    print(n)

