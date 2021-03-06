from functools import lru_cache
 
@lru_cache(maxsize=10)
def fib(n):
	if n <= 2:
    		return n
	return fib(n - 1) + fib(n - 2)
 
print([fib(i) for i in range(1000)])
print(fib.cache_info())