import logging

def logging_decorator(func):
    def decor(*args, **kargs):
        print("Running...")
        print(f"Function name = {func.__name__}, args = {args}, kargs ={kargs}")
        result = func(*args, **kargs)
        print(f"Result of {func.__name__} is {result}")
        return result 
    return decor


@logging_decorator
def add(a, b):
    return a + b

print(add(2 , 3))
