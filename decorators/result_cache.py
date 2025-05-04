def result_cache(func):
    cache = {}

    def decor(*args, **krgs):
        keys = (args, tuple(krgs.items()))
        print(f"Keys are {keys}")

        if keys in cache:
            print("Result is reurned from the cache")
            return cache.get(keys)
        
        result = func(*args, **krgs)
        cache[keys] = result

        return result

    return decor

@result_cache
def add(a, b):
    return a + b


print(add(1, 3))
print(add(7 , 2))
print(add(1, 3))