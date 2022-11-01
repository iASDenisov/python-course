'''
https://stepik.org/lesson/265082/step/3?unit=246030
'''
n,k = int(input()), int(input())
                        
if n > k:
    print('NO')                       
elif n < k:
    print('YES')
else:
    print("Don't know")
    
#n, k = int(input()), int(input())
#print("Don't know" if n == k else "YES" if n < k else "NO")