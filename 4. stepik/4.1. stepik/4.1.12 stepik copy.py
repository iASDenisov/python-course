'''
https://stepik.org/lesson/265081/step/12?unit=246029
'''
a,b,c = int(input()),int(input()),int(input())
s = 0
if a >= 1 and b >=1 and c >=1:
    s = sum([a,b,c])
    print(s)
elif a>=1 and b>=1 and c < 1:
    s = sum([a,b])
    print(s)
elif a>=1 and c>=1:
    s = sum([a,c])
    print(s)
elif b>=1 and c>=1:
    s = sum([b,c])
    print(s)
elif c>=1 and a<1 and b<1:
    s = c
    print(s)
else:
    print('0')