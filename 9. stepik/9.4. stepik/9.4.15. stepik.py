# https://stepik.org/lesson/303083/step/15?unit=284990

s = input()
a = s.find('h')
b = s.rfind('h')
c = s[a:b+1] # # Получаем текст между начальным и конечным индексом
print(s.replace(c,''))

