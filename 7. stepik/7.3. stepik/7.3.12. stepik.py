# https://stepik.org/lesson/294243/step/12?unit=275922

n = int(input())
s = 0
for i in range(1,n+1):
    if i % 2 == 0:
        s -= i
    elif i % 2 !=0:
        s += i
print(s)
