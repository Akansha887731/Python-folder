import time

def check_cache_expiry(expiry_time = 2):
    def wrapper(func):
        cache = {}

        def decor(*args, **kargs):
            keys = (args, tuple(kargs.items()))
            print(keys)
            print(cache)

            if keys in cache:
                value = cache.get(keys)
                time_diff = abs(value.get('stored_timestamp') - time.time())
                if time_diff < expiry_time:
                    print(f"Fetching from the cache for {keys}")
                    return value.get('result')
                else:
                    print(f"Cache expired for {keys} because last update time was {time_diff:.2f} seconds ago.")
                    print(f"The key {keys} is not in the cache (after expiry check).") # Optional: Clarify it's being recalculated
            else:
                print(f"The key {keys} is not in the cache")

            result = func(*args, **kargs)
            cache[keys] = {'stored_timestamp': time.time(), 'result': result}
            return result

        return decor
    return wrapper

@check_cache_expiry(expiry_time = 5)
def add(a, b):
    print("Calculating...")
    return a + b

print(add(3, 2))
print(add(3, 2))
time.sleep(6)
print(add(3, 2))
print(add(5, 6))