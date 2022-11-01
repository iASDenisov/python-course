'''
https://stepik.org/lesson/265083/step/12?unit=246031
'''
a = int(input())
b = int(input())
c = int(input())
if (a < (b + c)) and (b < (a + c)) and (c < (a + b)):
    print("YES")
else:
    print("NO")