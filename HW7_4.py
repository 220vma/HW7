from functools import wraps

def decorator(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        print(f.__name__, args, kwargs)
        return f(*args, **kwargs)
    return wrapper

@decorator
def f(a):
    '''
    arg a
    return a
    '''
    return a

print(f'original: {f.__name__}, {f.__doc__}')