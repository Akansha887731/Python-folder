def fac(n):
    a = 1
    for i in range(1, n):
        a = a * i
        yield a

r = fac(5)

l = [j for j in r]
print(l)
