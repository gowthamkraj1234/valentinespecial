# Dictionary keys should be immutable
# a={}
# print(type(a))

# b=dict()
# print(type(b))

# fruits={1:"Apple",2:"Mango",3:"Grapes",4:['Banana'],5:"Strawberry"}
# print(fruits)
# print(fruits.get(3))
# print(fruits[4])
# fruits[2]="Kiwi"
# print(fruits)

#personal record dictionary
# record={'Name':"M K Anirudha","Age":21,"YOB":2004,"College":"MIT Mysore","Skills":["Python","C","DSA","Machine Learning"]}
# record["Age"]="Twenty-One"
# record["Skills"][1]="Java"  # To add new elements to a list value, can use append menthod, for ex: record["Skills"].append(AI) 
# record["USN"]="4MH22IS046"
# print(record)

#update
# record.update({"Skills":["Python","DSA"]})
# print(record)
# new_detail={'comapny':'HP'}
# record.update(new_detail)
# print(record)

#Membership operators
# car={"Brand":"Ford","Model":"Mustang","Owner":"Hemanth"}
# if car["Owner"]=="Hemanth":
#     print("Correct owner")

#Iteration
# record={'Name':"M K Anirudha","Age":21,"YOB":2004,"College":"MIT Mysore","Skills":["Python","C","DSA","Machine Learning"]}
# for key in record.keys():
#     print(key)
# for value in record.values():
#     print(value)
# for key,value in record.items():
#     print(key,value)

#Nested Dictionary
# record={"siddu":{"college":"PES","loaction":"hunsur","age":22},
#         "rahul":{"college":"MIT","location":"mysore","age":21},
#         "rohan":{"college":"MIT","location":"mandya","age":21}}
# print(record["rahul"])
# print(record["siddu"])
# record["rohan"]["location"]="Bangalore"
# print(record)

# del record["rahul"]["age"]
# print(record["rahul"])

# for key,value in record.items():
#     print('Dictionary',key+":")
#     for k,val in value.items():
#         print(k+" -->",val)

#Assignment
sentence="Look into my eyes and talk and say I like you why is that so"
word_dictionary={}
words=sentence.split(" ")
for word in words:
    word_dictionary[word]=words.count(word)
print(word_dictionary)