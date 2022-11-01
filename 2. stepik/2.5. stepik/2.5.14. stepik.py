'''
https://stepik.org/lesson/284816/step/14?unit=266160
'''
num = int(input())
a = num // 100
b = (num % 100) // 10
c = num % 10  
print(a,b,c,sep='',end='\n')
print(a,c,b,sep='',end='\n')
print(b,a,c,sep='',end='\n')
print(b,c,a,sep='',end='\n')
print(c,a,b,sep='',end='\n')
print(c,b,a,sep='',end='\n')

# a,b,c = input()
# print(a+b+c, a+c+b, b+a+c, b+c+a, c+a+b, c+b+a, sep='\n')
