import time

def timer(f):
        def tmp(*args, **kwargs):
                t = time.time()
                res = f(*args, **kwargs)
                print(f'Время выполнения: {time.time() - t}')
                return res
        return tmp


@timer
def func(x, y):
        l = []
        for i in range(y):
                l.append(x)

func(0, 10_000_000)