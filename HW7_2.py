def memorize(f):
    cache = {}
    def wrapper(*args):
        print(args)
        if args not in cache:
            print('Кэш пустой')
            cache[args]=f(*args)
        else:
            print('Кэш полный')
        return cache[args]
    return wrapper

 
@memorize
def f(x, y):
	l = []
	for i in range(y):
    		l.append(x)
 
f(0, 10_000_000)
f(0, 10_000_000)
f(0, 10_000_000)
f(0, 10_000_000)
f(0, 10_000_000)