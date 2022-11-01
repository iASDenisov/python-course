#https://stepik.org/lesson/327207/step/9?unit=310501

lst1 = list()
lst2 = list()
for i in range(int(input())):
    lst1.append(int(input()))
    lst2.append(lst1[i] ** 3 )
print(lst2)