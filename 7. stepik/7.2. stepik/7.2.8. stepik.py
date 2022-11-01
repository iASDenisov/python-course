# https://stepik.org/lesson/265120/step/8?unit=246069

m,n = int(input()),int(input())
if m < n:
    for i in range(m,n+1):
        print(i)
else:
    for i in range(m,n-1,-1):
        print(i)