'''
https://stepik.org/lesson/265081/step/11?unit=246029
'''
y = int(input())
if y <= 13 and y >= 1:
    print('детство')
elif y >= 14 and y <=24:
    print('молодость')
elif y >= 25 and y <= 59:
    print('зрелость')
else:
    print('старость')
# n = int(input()); print("детство" if n <= 13 else "молодость" if n <= 24 else "зрелость" if n <= 59 else "старость")