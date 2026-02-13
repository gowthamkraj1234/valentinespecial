# # #list
# # a=[1,2,3,4,5]
# # print(a)


# # sentence="Gowtham likes to live in his native place"
# # words=sentence.split()
# # word_list=[]
# # count_list=[]
# # for word in words:
# #     word_list.append(word)
# #     count_list.append(len(word))
# # print(len(words))
# # print(word_list)
# # print(count_list)

# # word="Python Training4678"
# # lower_count,upper_count,num_count=0,0,0
# # for char in word:
# #     if char.islower():
# #         lower_count+=1
# #     elif char.isupper():
# #         upper_count+=1
# #     elif char.isdigit():
# #         num_count+=1
# # print("Lower case count:",lower_count)
# # print("Upper case count:",upper_count)
# # print("Number count:",num_count)


# # #to print sum of numbers in list
# # numbers=[20,30,40,50,60,70]
# # sum=0
# # for num in numbers:
# #     sum+=num
# # print("Sum of numbers in the list:",sum)

# # #Iterate over nested list
# # companies=[['Microsoft','Googgle','Hewlett Packard'],['Infosys','Wipro','TCS'],['Honda','Hyundai','Kia']]
# # for company_group in companies:
# #     for company in company_group:
# #         print(company)

# # name_list=[]
# # print(type(name_list))

# # name_list=list()
# # print(type(name_list))

# #Ways Of Creating a List -> name_list=[] or name_list=list() or using List Comprehension or Type casting different data types like, first_name="Rakshith" then list(first_name)
# name_list=[]
# print(type(name_list))

# name_list=list()
# print(type(name_list))

# name="GOWTHAM K"
# print(list(name))


# #Adding data into a list
# car_brands=["BMW","Mercedes","Kia","Suzuki","Hyundai","Tata"]
# print(car_brands)

# #Append
# car_brands.append("AUDI")
# print(car_brands)

# #Appending heterogeneous data
# car_brands.append(1995)
# car_brands.append(2005)
# print(car_brands)

# car_brands.append(["Ferrari","Lambhorgini"])
# print(car_brands)

# car_brands.append({"TATA":"NEXON","KIA":"SELTOS"})
# print(car_brands)

# #Extend
# places=["Bengaluru","Bidadi","Ramanagara","Channapattana","Maddur","Mandya"]
# print(places)

# #places.extend('Srirangapattana') #This adds each character of the string as element of list
# places.extend(['Srirangapattana'])
# print(places)
# places.extend(['Mysuru Outer Ring Road','Mysuru'])
# print(places)

# #Insert
# places[1]="Kengeri"
# print(places)
# places.insert(2,'Bidadi')
# print(places)

# #Count Method Returns the occurance of the element
# fruits = ["apple", "banana", "cherry","apple"]
# print(fruits.count("apple"))

# #Copy-> Returns the shallow or temperory copy of the list and will not affect each other
# new_fruits = fruits.copy()
# print(fruits)
# print(new_fruits)

# fruits.remove("apple")
# print(fruits)
# print(new_fruits) #So when copy method is used copied list is not affected when we modify original list.But it is dfferent when we use assignment operator

# #Sort   
# new_fruits.sort()
# print(new_fruits)

# #Clear
# new_fruits.clear()
# print(new_fruits)

# #Iterating a list
# places=["Bengaluru","Bidadi","Ramanagara","Channapattana","Maddur","Mandya","Mysuru"]
# for place in places:
#     print(place)

# for place in range(len(places)):
#     print(places[place])

# mix_list=['gowtham','rakshith',['ram','shyam']]
# print(mix_list)
# for item in mix_list:
#     if isinstance(item, list):
#         for sub_item in item:
#             print(sub_item)


# #match case
# shape = "circle"

# match shape:
#     case "square":
#         print("4 sides")
#     case "rectangle":
#         print("Opposite sides equal")
#     case "circle":
#         print("No sides")
#     case _:
#         print("Invalid shape")


shape = "circle"

if shape == "square":
    print("4 sides")
elif shape == "rectangle":
    print("Opposite sides equal")
elif shape == "circle":
    print("No sides")
else:
    print("Invalid shape")


#zip function
names = ["Ram", "Shyam", "Mohan"]
marks = [85, 90, 78]

z = zip(names, marks)

for n, m in z:
    print(n, m)




roll = [1, 2, 3]
names = ["A", "B", "C"]
marks = [80, 85, 90]

for r, n, m in zip(roll, names, marks):
    print(r, n, m)
