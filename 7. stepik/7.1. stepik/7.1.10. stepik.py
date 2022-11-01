# https://stepik.org/lesson/265118/step/10?unit=246067

m,p,n = float(input()),float(input()),int(input())

for i in range(n):
    print(i + 1, m)
    m = m + p / 100 * m