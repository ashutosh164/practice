# a = [True, True, True, True]
# b = [False, False, False]
# print(any(a))
# print(all(a))
# print(any(b))
# print(all(b))
#
# numbers = [2,4,6]
# even = lambda x: x % 2 == 0
#
# result = [even(i) for i in numbers]
# # if any(result):
# #     print('At list one number is Even')
# # else:
# #     print('No Number is even')
# #
# # if all(result):
# #     print('All number are even')
#
# if any(result):
#     print('At list one number is Even')
# else:
#     print('No Number is even')
#
# if all(result):
#     print('All number are even')


from gtts import gTTS

import os


mytext = 'Welcom to python '
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save('welcom.mp3')
os.system('welcom.mp3')




