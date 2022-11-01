# https://stepik.org/lesson/265120/step/10?unit=246069

for i in range(int(input()),int(input())+1):
    if i % 17 == 0 or i % 10 == 9 or (i % 3 == 0 and i % 5 == 0):
        print(i)