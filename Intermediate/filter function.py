def add(x):
    return x + 7


def isOdd(x):
    return x%2 != 0


a = [1,2,3,4,5,6,7,8,9]
b = list(filter(isOdd, a))
print(b)
c = list(map(add, b))
print(c)













