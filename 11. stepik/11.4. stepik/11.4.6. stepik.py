# # https://stepik.org/lesson/328948/step/6?unit=312239

n,list1,list2 = int(input()),[],[]
for i in range(n):
    list1.append(input())
a = input()
for i in list1:
    if a.lower() in i.lower():
        print(i)