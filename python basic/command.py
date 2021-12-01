command = ''
while command.lower() != 'quite':
    command = input('>')
    print(f'Echo: {command}')
    if command.lower() == 'quite':
        break
    elif command.lower() == 'q':
        break

#
# if command.lower() != 'quite':
#     while True:
#         command = input('>')
#         print(f'Echo: {command}')









