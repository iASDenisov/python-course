# https://stepik.org/lesson/328948/step/4?unit=312239

list1 = []
for i in range(int(input())):
    list1.append(int(input()))
list1.remove(min(list1))
list1.remove(max(list1))
print(*list1,sep='\n')