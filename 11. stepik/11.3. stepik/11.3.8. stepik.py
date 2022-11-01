# https://stepik.org/lesson/327207/step/8?unit=310501

lst = []
for i in range(ord('z') - ord('a') + 1):
    lst.append(chr(ord('a') + i) * (i + 1))
print(lst)