# https://stepik.org/lesson/327207/step/11?unit=310501


lst1 = list()
lst2 = list()
for i in range(int(input())):
    lst1.append(int(input()))
    if i > 0:
        lst2.append(lst1[i] + lst1[i-1])
del lst1 # удаляем ненужный список
print(lst2)