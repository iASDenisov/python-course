# https://stepik.org/lesson/327207/step/12?unit=310501

lst1 = list()
for i in range(int(input())):
    lst1.append(int(input()))
del lst1[1::2] 
print(lst1)

