# https://stepik.org/lesson/298795/step/7?unit=280622

a = int(input())
for i in range(1,a+1):
    for j in range(1,10):
        print(f'{i} + {j} = {i+j}',end='\n')
    print()
