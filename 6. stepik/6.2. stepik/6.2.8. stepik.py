# https://stepik.org/lesson/265115/step/8?unit=246063
a = input()
b = input()
c = input()

if min (len(a), len(b), len(c)) == len(a):
    print(a)
elif min (len(a), len(b), len(c)) == len(b):
    print(b)
else:
    print(c)
if max (len(a), len(b), len(c)) == len(a):
    print(a)
elif max (len(a), len(b), len(c)) == len(b):
    print(b)
else:
    print(c)
    
# cities = ["city11", "city1", "city111"]
# cities.sort(key=len)
# print(cities[0], cities[-1])