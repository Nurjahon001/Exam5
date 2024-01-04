

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        d = [i for i in range(1,result) if i % 2 == 0]
        return result
    return wrapper



@timer
def example_function():
    time.sleep(2)

print(timer(2))
example_function()