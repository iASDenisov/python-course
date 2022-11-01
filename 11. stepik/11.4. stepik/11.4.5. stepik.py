# # https://stepik.org/lesson/328948/step/5?unit=312239

list1 = []
for i in range(int(input())):
    a = input()   
    if a not in list1:
        list1.append(a)
print(*list1,sep='\n')