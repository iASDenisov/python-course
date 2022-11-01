# https://stepik.org/lesson/294243/step/6?unit=275922

n = int(input()) # кол-во чисел для суммирования
s = 0 # счетчик суммы
for i in range(1,n+1):
    s += int(input()) # сумма введенных чисел
print(s)