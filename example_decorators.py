from datetime import datetime


# def outer():
#     def inner():
#         pass
#     return inner


def     upper(fn):
    def inner(name):
        # print(f'Function: {fn.__name__} was called at {datetime.now()}')
        result = fn(name.title())
        # result = 'dupa'
        return result

    return inner

def reverse(fn):
    def wrapper(text):
        return fn(text[::-1])
    return wrapper


@reverse
def say_hello(name):
    return f'Hello {name}'

@reverse
@upper
def say_bye(name):
    return f'Bye{name}'


# print(say_hello('jaroslaw'))
# print(say_hello('lech'))

# memoizing

def cache(func):
    memo = {}
    print('cache', 20 * '-')
    def wrapper(*args):
        if args not in memo:
            print('save', 20 * '#')
            memo[args] = func(*args)
        return memo[args]

    return wrapper
@cache
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(10))
print(factorial(10))

class X:
     def __init__(self):
         self._value = 42

     @property
     def value(self):
         return self._value
     @value.setter
     def value(self, new_val):
         self._value = new_val

















