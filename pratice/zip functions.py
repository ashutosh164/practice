name = ['ashu', 'jilu', 'silu', 'bulu', 'deepak']
age = [24, 22, 21, 29, 6]


# for i in range(len(name)):
#     print(f'Name: {name[i]}, Age: {age[i]}')


# print(list(zip(name, age)))

for i, j in zip(name, age):
    print(f'Name: {i}, Age: {j}')

print('------------------------------------')

sales = [500, 600, 7000, 45455, 4453, 950]
cost = [200, 444, 1999, 3434, 34, 30]


for i, j in zip(sales, cost):
    print(f'Sales: {i}, Cost: {j}, Profit: {i-j} ')





