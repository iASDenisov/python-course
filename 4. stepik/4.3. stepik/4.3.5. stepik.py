'''
https://stepik.org/lesson/265082/step/5?unit=246030
'''
a,b,c = int(input()),int(input()),int(input())
if a < b and b < c or c < b and b < a:
    print(b)
elif b < c and c < a or a < c and c < b:
    print(c)
elif c < a and a < b or b < a and a < b:
    print(a)
