#TUPLE CREATION
name_tuple=()
print(type(name_tuple))

name_tuple=("a")
print(type(name_tuple))

name_tuple=("a",) #Comma mandatory
print(type(name_tuple))
print(name_tuple)

name_tuple=("a","b")
print(type(name_tuple))
print(name_tuple)

# company_tuple=tuple('microsoft','google') #Error because this constructor takes only one element or one comma
# print(type(company_tuple))
# print(company_tuple)

company_list=['microsoft','google','amazon']
print(type(company_list))
print(company_list)
company_tuple=tuple(company_list)
print(type(company_tuple))
print(company_tuple)

#Tuple can have heterogeneous data
hetero_tuple=('Rakshith Gowda M R',20,'7th Sem',[86,90,98,199,77,84])
print(type(hetero_tuple))
print(hetero_tuple)

print("Allowed Tuple Mutations")
print(hetero_tuple[0])
print(hetero_tuple[0:3])

#You can modify the list within tuple through indexes So you can apply all the methods that is applicable to list
print(hetero_tuple[3][3])
hetero_tuple[3][2]=21
print(hetero_tuple[3])
print(hetero_tuple)

#You can apply mutations by converting a tuple into list and after modifications convert it back to tuple
hetero_list=list(hetero_tuple)
print(hetero_list)
hetero_list[2]="8th Sem"
print(hetero_list)
hetero_list[3].remove(77)
print(hetero_list)
hetero_tuple=tuple(hetero_list)
print(hetero_tuple)


#Packing & Unpacking

#Packing
fruits='Apple','Banana','Orange'
print(type(fruits))
print(fruits)

#Unpacking
fruits='Apple','Banana','Orange','Strawberry','[100,200,300,400]'
print(fruits)
print("-->Unpack each value into a variable")
red,yello,saffron,pink,cost=fruits
print(red)
print(yello)
print(saffron)
print(pink)
print(cost)
print("-->Unpack only first value into a variable")
red,*fruit=fruits
print(red)
print(fruit)
print("-->Unpack first and last value into a variable")
red,*fruit,cost=fruits
print(red)
print(fruit)
print(cost)
print("-->Unpack last two values into a variable")
*fruit,pink,cost=fruits
print(fruit)
print(pink)
print(cost)


fruits = ["apple","banana","mango"]
fruit=("apple","banana","mango")
print(fruits.__sizeof__())
print(fruit.__sizeof__())

#Count method is supported since it is not mutation method only read only
print(fruit.count("apple"))

#Iterating over a tuple
for fruitee in fruit:
    print(fruitee)