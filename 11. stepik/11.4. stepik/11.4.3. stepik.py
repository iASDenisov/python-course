# https://stepik.org/lesson/328948/step/3?unit=312239

n = int(input())
x = [] 
for i in range(n):
    x.append(int(input()))
for i in x:
    print(i)
print()
for i in range(n):
    print((x[i] ** 2) + (2 * x[i]) + 1, end = '\n')