# https://stepik.org/lesson/294243/step/7?unit=275922

from math import log
n = int(input())
d = float(0)
for i in range(1,n + 1):
    d += (1 / i)
print(d-log(n))