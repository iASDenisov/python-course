# https://stepik.org/lesson/327207/step/10?unit=310501

n = int(input())
i = 0
list1 = list()
for i in range(n+1):
    if i > 0 and n % i == 0:
        list1.append(i)
print(list1)

