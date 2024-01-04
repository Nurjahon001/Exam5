def decorator_func(original_func):
    def wrapper(*args,**kwargs):
        v=original_func(*args,**kwargs)
        d=[]
        k=[]
        for i in d:
            if i.isdigit():
                if i< 2:
                    return False
                for j in range(2, int(i ** 0.5) + 1):
                    if i % j == 0:
                        return False
                k.append(i)
        return d
    return wrapper

@decorator_func
def sonlar(son):
    return son
print(sonlar([2,6,-7,8,3,5,"dsdcscs"]))



