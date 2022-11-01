# https://stepik.org/lesson/284101/step/13?unit=265440

s = input()
counter = 0
s1 = ''
for i in range(len(s)):
    if s1 == s[i]:
        counter += 1
    s1 = s[i]
print(counter)
