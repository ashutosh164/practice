square = lambda x, y: x * y
print(square(4, 7))

a = lambda *args: sum(args)

print(a(2,4,6,7,8,5))

print((lambda x: x**3)(5))
print((lambda x,y: x + y)(5,7))

numbers = [8,33,5,55,34,8,65,3,4,756]


def filter_fun(x):
    return x % 2 == 0


even = filter(lambda x: x%2 == 0, numbers)
print(list(even))


square = list(map(lambda x: x ** 2, numbers))
print(square)

print('-------------------------')






