#

s = input()                  
k = 0                         

for i in range(len(s)):       
    if s[i] != s[i].upper():  
        k+=1                
print(k)