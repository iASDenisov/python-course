# https://stepik.org/lesson/303083/step/10?unit=284990

a,b = int(input()), 0
counter = 0
while b != a:
    if str(input()).count('11') >= 3:
        counter +=1
    b += 1
print(counter)