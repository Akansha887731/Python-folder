def return_value_type(func):
    def decor(*args, **kargs):
        result = func(*args, **kargs)
        return type(result)
    return decor

@return_value_type
def add(a, b):
    return a + b

print(add(4, 6))