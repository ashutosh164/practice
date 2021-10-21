mynames = ['ashu','jilu','bulu','lilu','anil','j']

counter = 0
for i in mynames:
    print(f'{counter}: {i}')
    counter += 1
print('-------------enumoration--------------')


for i,j in enumerate(mynames):
    print(f'{i}: {j}')

print('-----------------------------------')

print(dict(enumerate(mynames)))


