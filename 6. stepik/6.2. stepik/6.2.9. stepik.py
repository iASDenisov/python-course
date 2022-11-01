# https://stepik.org/lesson/265115/step/9?unit=246063
a,b,c=len(input()),len(input()),len(input())
print("YES" if (2 * b - c - a) == 0 or (2 * c - b - a)== 0 or (2 * a - b - c) == 0 else "NO")