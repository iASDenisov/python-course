# https://stepik.org/lesson/265122/step/4?unit=246071
n = int(input())

while n:           # False = 0 , True = все что не 0
    i = n % 10     # получить последнюю цифру    
    n = n // 10    # удалить последнюю цифру из числа         
    print(i)