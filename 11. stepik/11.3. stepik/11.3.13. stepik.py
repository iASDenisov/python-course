# https://stepik.org/lesson/327207/step/13?unit=310501

n = input()
list1 = []
for i in range(n):
    list1.append(input())
k = input()
stroka = ''
for i in list1:
    if len(i) >= k:
        stroka += i[k-1]
print(stroka)
    