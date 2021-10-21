num = [2,4,5,7,6,3,8]


def square(x):
    return x * x


b=[]
for i in num:
   b.append(square(i))

print(b)

c = [square(i) for i in num]
print(c)

# apply map functions

c = map(str, num)
print(list(c))










