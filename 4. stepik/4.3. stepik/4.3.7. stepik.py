'''
https://stepik.org/lesson/265082/step/7?unit=246030
'''
w = int(input())
if w < 60:
    print('Легкий вес')
elif w >= 60 and w < 64:
    print('Первый полусредний вес')
else:
    print('Полусредний вес')