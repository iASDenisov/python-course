# https://stepik.org/lesson/265121/step/10?unit=246070

ctr = 0
text = input()
while text not in ('стоп', 'хватит','достаточно'):
    ctr += 1
    text = input()
print(ctr)