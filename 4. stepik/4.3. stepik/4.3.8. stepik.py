'''
https://stepik.org/lesson/265082/step/8?unit=246030
'''
'''
https://stepik.org/lesson/265082/step/8?unit=246030
'''
a,b,o = int(input()),int(input()),str(input())
if o == "/" and b == 0:
    print('На ноль делить нельзя!')
else:
    if o =='+':
        print(a+b)
    elif o == '-':
        print(a-b)
    elif o == "*":
        print(a*b)
    elif o == '/':
        print(a/b)
    else:
        print('Неверная операция') 
        
# a, b, op = (input() for _ in range(3))
# print("Неверная операция" if op not in ("+", "-", "*", "/") else "На ноль делить нельзя!" if op=='/' and b=='0' else eval(a+op+b))