# https://stepik.org/lesson/328948/step/7?unit=312239

# кол-во строк n для ввода в список
# ввод n строк(цикл)
# кол-во поисковых запросов k
# ввод поисковых запросов(цикл)
# сравнение запроса с элементами массива(списка)
# если входит - выводим

n, list1, list2 = int(input()), [], []
for i in range(n):
    list1.append(input())
k = int(input())
for i in range(k):
    list2.append(input())
for i in list1:
    for j in list2:
        if j.lower() not in i.lower():
            break
    else:
        print(i)
