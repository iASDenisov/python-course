# https://stepik.org/lesson/265121/step/9?unit=246070

text = input()
while str.lower(text) != "конец":
    print(text,sep='\n')
    text = input()
    
# text = input()
# while 'конец' != text != 'КОНЕЦ':
#     print(text)
#     text = input()

# while x not in ('КОНЕЦ', 'конец'):
#   print(x)
#   x = input()