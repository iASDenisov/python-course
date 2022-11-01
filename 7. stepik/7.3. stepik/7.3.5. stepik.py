# https://stepik.org/lesson/294243/step/5?unit=275922

count = 0
for i in range(int(input()),int(input())+1):
    if i ** 3 % 10 == 4 or i ** 3 % 10 == 9:
        count += 1
print(count)