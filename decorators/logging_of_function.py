import logging

def logging_decorator(func):
    def decor(*args, **kargs):
        print("Running...")
        print(f"Function name = {func.__name__}, args = {args}, kargs ={kargs}")
        result = func(*args, **kargs)
        print(f"Result of {func.__name__} is {result}")
        return result 
    return decor

import time
from datetime import datetime

def time_calculator(func):
    def decor(*args, **kwargs):
        start_time = datetime.now()
        print('Time calculation started...')
        result = func(*args, **kwargs)
        end_time = datetime.now()
        print(f"The function took {end_time - start_time}")
        return result
    return decor


@logging_decorator
@time_calculator
def add(a, b):
    return a + b

print(add(2 , 3))
