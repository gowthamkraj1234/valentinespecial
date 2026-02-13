# #strings
# text='hello world'
# print(text)

# #capitalize
# print(text.capitalize())

# #upper
# print(text.upper())
# # upper_text = text.upper()
# # print(text)
# # print(upper_text)


# #lower
# print(text.lower())

# #to find length of string
# text='python learning is fun'
# print(len(text))

# #strip method
# msg='   hello world   '
# print(len(msg))
# print(msg.strip())
# print(msg.lstrip())
# print(msg.rstrip())

# #find method
# text='python learning is fun'
# print(text.find('o'))
# print(text.find('z'))  # returns -1 if not found
# print(text.find('learning'))

# #rfind method
# print(text.rfind('s'))  

# #index method
# print(text.index('l'))

# #startswith method
# print(text.startswith('python'))
# print(text.startswith('P')) #case-sensitive

# #endswith method
# print(text.endswith('fun'))
# print(text.endswith('Fun')) #case-sensitive

# #replace method
# print(text.replace('fun', 'awesome'))
# print(text.replace(' ', '_'))
# print(text)  # original string remains unchanged

# #split method
# new_text1 = text.split(' ') #split by space
# print(new_text1)
# new_text2 = text.split('is') #split by 'is
# print(new_text2)

# #maxsplit method
# new_text3 = text.split(' ', 2) #split by space, max 2 splits
# print(new_text3)

# #isupper method
# greet1='HELLO'
# print(greet1.isupper())
# greet2='Hello'
# print(greet2.isupper())

# #islower method
# greet3='hello'
# print(greet3.islower())
# greet4='Hello'
# print(greet4.islower())

# #isdigit method
# num1='12345'
# print(num1.isdigit())
# num2='123a45'
# print(num2.isdigit())
# num3='12.45'
# print(num3.isdigit())

# #string indexing
# text='python'
# print(text[0])  # prints 'p'
# print(text[-1])  # prints 'n'
# print(text[2:5])  # prints 'tho'
# print(text[-5:-1])  # prints 'ytho'
# print(text[:3])  # prints 'pyt'
# print(text[0:5:2])  # prints 'pto' (every second character from index 0 to 5)      [start:end:step]

# #isalpha method
# word1='Hello'
# print(word1.isalpha())
# word2='Hello123'
# print(word2.isalpha())
# word3='Hello World'
# print(word3.isalpha())

# #istitle method
# title1='Hello World'
# print(title1.istitle())
# title2='Hello world'
# print(title2.istitle())

# #isalnum method
# alnum1='Hello123'
# print(alnum1.isalnum())
# alnum2='Hello 123'
# print(alnum2.isalnum())
# alnum3='Hello@123'
# print(alnum3.isalnum())
# alnum4='HelloWorld'
# print(alnum4.isalnum())