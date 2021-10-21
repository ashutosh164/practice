def fun(x):
    return x + 5


a = lambda x: x+5
b = lambda i, j: i * j

print(b(23, 45))

print(a(45))

a = [1,2,3,4,5,6,7,8,9]
new = list(map(lambda x: x+5,a))
print(new)

b = list(filter(lambda x: x%2==0,a))
print(b)








