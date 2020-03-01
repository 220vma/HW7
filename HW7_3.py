def tracer(f):
   count = 0
   def wrapper(*args, **kwargs):
       nonlocal count
       count += 1
       print(f'Вызовов для функции {f.__name__}: {count}')
       return f(*args, **kwargs)
   return wrapper

@tracer
def f1(a, b, c):
   print(a + b + c)

@tracer
def f2(a, b):
   print(a // b)

f1(2, 10, 9)
f1(a = 10, b = 7, c = 18)
f2(1, -3)
f2(6, b = 3)