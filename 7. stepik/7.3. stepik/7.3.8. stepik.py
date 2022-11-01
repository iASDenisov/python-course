# https://stepik.org/lesson/294243/step/8?unit=275922

count = 0
for i in range(1,int(input())+1):
    if i ** 2 % 10 == 2 or i ** 2 % 10 == 5 or i ** 2 % 10 == 8:
        count += i
print(count)