ctr = 0 # счетчик
for i in range(1,10+1):
    a = int(input())
    if a % 2 == 0:
        ctr += 1
if ctr == 10:
    print("YES")
else:
    print("NO")

# answer = 'YES'
# for _ in range (10):
#    if int(input()) % 2:
#       answer = 'NO'
#       break
# print(answer)