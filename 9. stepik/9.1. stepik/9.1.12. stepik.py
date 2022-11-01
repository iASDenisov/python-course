# https://stepik.org/lesson/284101/step/12?unit=265440

s = input()
sim1,sim2 = 0,0
for i in range(len(s)):
    if s[i] in '+':
        sim1 += 1
    elif s[i] in '*':
        sim2 += 1
print(f'Символ + встречается {sim1} раз\nСимвол * встречается {sim2} раз')

# s = input()
# for i in ['+','*']:
#    print(f'Символ {i} встречается {s.count(i)} раз')

# s = input()
# print(f"Символ + встречается {s.count('+')} раз")
# print(f"Символ * встречается {s.count('*')} раз")