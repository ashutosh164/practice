for i in range(5):
    for j in range(5):
        if j > 1:
            break
        print(f'({i},{j})')


print('--------------------')


for i in range(10):
    if i % 2:
        continue
    print(i)

print('-----------------')

a = 0
while a < 10:
    a += 1

    if a % 2:
        continue
    print(a)

print('-----------------')


def fun(name, message='hii'):
    return f'{message} {name}'


print(fun('ashu','hello'))


def fun2(price, discount):
    return price - (price * (discount/100))


print(fun2(100, 10))

print('------------------')


import time


def count_down(start):
    print(start)
    next = start -1
    if next > 0:
        time.sleep(1)
        count_down(next)
    if next == 0:
        print('happy new year')


count_down(5)
print('-----------------------')


def fun3(first_name,last_name,format):
    return format(first_name,last_name)


a = fun3('ashutosh','pradhan',lambda x,y:f'{x} {y}')
print(a)




