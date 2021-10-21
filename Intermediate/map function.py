a = [1,2,3,4,5,6,67,9]


def fun(x):
    return x * x

# b = []
# for x in a:
#     b.append(fun(x))
# print(b)


print(list(map(fun, a)))

print([fun(i) for i in a])

print([fun(i) for i in a if i%2==0]) 




