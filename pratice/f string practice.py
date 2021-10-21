name = 'ashu'
age = 7
num = 24.344444466
# here there are 3 types of strings format

print('hello my name is ' + name + 'and i am ' + str(age))
print('hello my name is %s and i am %d and my number is %.2f' %(name, age, num))
print('hello my name is {} ang i am {}'.format(name,age))
print(f'hello my name is {name} and i am {age} ears old')
print(f"hello my name is {name} and {'i am age enough'if age >= 18 else 'i am not matured'} to find a girlfriend and my favourite number is {num:.2f}")



