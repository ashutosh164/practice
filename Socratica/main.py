'''
Fibonacci Sequence

Write a functions that return nth term of fibonacci number
'''


def fun(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fun(n-1) + fun(n-2)


# for n in range(1, 11):
#     print(n, ':', fun(n))
#
# for n in range(1, 11):
#     print(n, ':', fun(n))

''' 
If i want to know the first 100 of fibonacci number then it is going to slow. so we have a solutions call  MEMOIZATION 
'''

fib_cache = {}


def fib(n):
    # if we have cached the value , then return it
    if n in fib_cache:
        return fib_cache[n]
    # computer the nth term
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fib(n-1) + fib(n-2)
# Cache the value and return it
    fib_cache[n] = value
    return value


# for i in range(1,101):
#     print(i, ':', fib(i))


'''
Another method of cacheing data
'''

from functools import lru_cache


@lru_cache(maxsize=1000)
def func(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return func(n-1) + func(n-2)


# for i in range(1,501):
#     print(i, ':', func(i))

'''
if input an negative number the our program is crash the what should we do know 
'''


@lru_cache(maxsize=1000)
def func2(n):
    if type(n) != int:
        raise TypeError('n must b a positive integer')
    if n < 1:
        raise ValueError('n must be a positive integer')
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return func2(n-1) + func2(n-2)


for i in range(1,51):
    print(i, ':', func2(i))