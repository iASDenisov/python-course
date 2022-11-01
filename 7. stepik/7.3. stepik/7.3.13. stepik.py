# https://stepik.org/lesson/294243/step/13?unit=275922

n1 = int(0)
n2 = int(0)
for i in range(1,int(input())+1):
    n = int(input())
    if n > n1 :
        n2 = n1
        n1 = n
    elif n > n2:
        n2 = n
print(n1,n2,sep='\n')