# https://stepik.org/lesson/303083/step/13?unit=284990

a,colvo,c = input(),0,'' # Colvo Переменная для кол-ва символов
for i in a:
    if a.count(i) >= colvo:
        colvo = a.count(i)
        c = i
print(c)        
