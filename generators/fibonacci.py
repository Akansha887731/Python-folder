def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b

r = fibonacci(10)

l = [j for j in r]
print(l)