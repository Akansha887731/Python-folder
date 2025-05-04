def next_palindrome(n):
    for i in range(n):
        if str(i) == str(i)[::-1]:
            yield i

r = next_palindrome(1000)

l = [j for j in r]
print(l)