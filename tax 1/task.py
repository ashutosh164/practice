# Remove duplicate tuples from list of tuples

# MMethod #1 : List comprehension

def remove_duplicate(a):
    return [i for i in (set(tuple(b) for b in a))]


a = [(1, 2), (5, 7), (3, 6), (1, 2)]
print(remove_duplicate(a))
print('-----------------------------')
# Method #2 : List comprehension (Efficient approach)


def fun(a):
    return list(set([i for i in a]))


print(fun(a))

# Method #3 : Python enumerate() method

# def fun1(a):
#     return