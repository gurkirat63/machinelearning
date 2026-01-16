import time
from functools import wraps

def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print("elapsed time: ", end-start)
        return result
    return wrapper    

def funcname(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Running Function: {func.__name__}")
        result = func(*args, **kwargs)
        return result
    return wrapper    

def print_output(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(result)
        return result
    return wrapper    

