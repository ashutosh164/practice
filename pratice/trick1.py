numbers = [18,3,2,5,34,45,34,46]
a = []
for i in numbers:
    if i % 2 == 0:
        a.append(i)

print(a)

# trick

b = [i for i in numbers if i % 2 == 0]
print(b)

print('######################')
a = [2,3,4,5,6,7]
b = [x ** 2 for x in a]
print(b)
c = [i * 5 for i in a]
print(c)

a = [x ** 2 for x in range(30) if x % 5 == 0]
print(a)

word = ['ashu','jilu','ailu','bulu','ayush']
a = [i.replace('a', 'A') if i.startswith('a') else i for i in word]
b = [i.upper() for i in word if i.startswith('a')]
c = [i.upper() if i.startswith('a') else i for i in word]
print(c)


