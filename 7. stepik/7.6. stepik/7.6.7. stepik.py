# https://stepik.org/lesson/298794/step/7?unit=280621

n = int(input())
for i in range(1,n+1):
    if n % i == 0 and i != 1:
        print(i)
        break
    
#n, a = int(input()), 2
#while n % a != 0:
#    a += 1
#print(a)  

    