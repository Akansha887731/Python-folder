import time
from datetime import datetime

def time_calculator(func):
    def decor(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.now()
        print(f"The function took {end_time - start_time}")
        return result
    return decor

@time_calculator
def add(a, b):
    time.sleep(5)
    return a + b

print(add(5, 65))
