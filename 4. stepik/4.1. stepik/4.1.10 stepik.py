'''
https://stepik.org/lesson/265081/step/10?unit=246029
'''
a,b,c,d = int(input()),int(input()),int(input()),int(input())
if a < b and a < c and a < d:
    print(a)
elif b < c and b < d:
    print(b)
elif c < d:
    print(c)
else:
    print(d)
#print(min(int(input()), int(input()), int(input()), int(input())))