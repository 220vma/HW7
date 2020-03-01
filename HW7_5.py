from functools import singledispatch

@singledispatch
def pt(arg):
    print(f'Тип параметра \'{arg}\': {type(arg)}')

@pt.register(int)
def i(arg):
    print(f'Int: {arg}')

@pt.register(list)
def l(arg):
    print(f'List: {arg}')

pt(1)
pt([1, 2])
pt('gdjfhd')