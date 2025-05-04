import tracemalloc

def check_memory(func):
    def wrapper(*args, **kargs):
        tracemalloc.start()
        result = func(*args, **kargs)
        snapshot = tracemalloc.take_snapshot()
        stats= snapshot.statistics('lineno')
        memory_usage = sum([stat.size for stat in stats])
        
        print(f"The {func.__name__} took a total space of {memory_usage} bytes.")
        tracemalloc.stop()
        return result
    return wrapper

@check_memory
def counting(a, b):
    c = [i for i in range(a, b)]
    return c

counting(1, 1000)