# https://stepik.org/lesson/265121/step/13?unit=246070

x,s = int(input()), 0
while x > 0 and x < 6:
    s += x == 5 # если х = 5 то s + 1
    x = int(input())
print(s)