# names=['Gowtham','rakhsith','ram','raj']
# new_name=[]
# for name in names:
#     new_name.append(name.upper())
# print(new_name)       

# names=['Gowtham','rakhsith','ram','raj']
# new_name=[name.upper() for name in names]
# print(new_name)

# word='human'
# new_word_list=[]
# for char in word:
#     new_word_list.append(char)
# print(new_word_list)

# word='human'
# new_word_list=[char for char in word]
# print(new_word_list)

names=["rakshith","john","stephen","lyka"]
new_list=[]
for name in names:
    new_list.append(name.upper())
print(new_list)

#LIST COMPREHENSION WAY SYNTAX--> output=[expression for item in iterable condition]
names=["rakshith","john","stephen","lyka"]
new_list=[name.upper() for name in names]
print(new_list)

#Another example
name="human"
new_word_list=[char for char in name]
print(new_word_list)

#Another example
name_list=['Sejal Sondur','Harshitha R','Anirudh MK','Hiteshwar P']
# new_namelist=[' '.join(name.split()[::-1]) for name in name_list]
new_name_list=[name.split(" ")[1]+" "+name.split(" ")[0] for name in name_list]
print(new_name_list)

#Example 2
name_list=['Sejal Sondur','Harshitha R','Anirudh MK','Hiteshwar P']
new_list=[name[::-1] for name in name_list]
print(new_list)

#Example 3
name_list=['Sejal Sondur','Harshitha R','Anirudh','Hiteshwar P']
city_list=['Sandur','Bangalore','Mandya','Doddaballapura']
new_list=[]
for i in range(0,len(name_list)):
    new_list.append([name_list[i],city_list[i]])
print(new_list)