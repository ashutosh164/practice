''' HOW WE CAN WRITE THE SUME OF PREVIOUS NUMBER '''


def fibonancci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b


fib = fibonancci(10)
for i in fib:
    print(i)


'''HOW WE CAN MULTPLY BY A NUMBER WITH WHOLE NUMBER OF INSIDE IN LIST'''

A = (1, 2, 3, 4, 5, 6)
B = map(lambda x: x*2, A)
print(list(B))

c = [x*2 for x in A]
print(c)

c = (3,5,6,7,6,8,9,0,3)

d = [x*5 for x in c]

print(d)

v = lambda x: x*2
print('-------------')
print(v(A))


a = (2,3,4,5,7,9,4)
b = map(lambda x: x*4, a)
print(list(b))



