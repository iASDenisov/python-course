# https://stepik.org/lesson/303083/step/11?thread=solutions&unit=284990

s=0
for c in input():
    if '0'<=c<='9': # сравниваем символ с 0-9
        s+=1
print(s)