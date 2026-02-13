sets={'a','b','c'}
print(sets)
print(sets[1]) # cannot be done as sets do not support indexing

snacks=['cola','chocolate','biscuit']
snack=set(snacks)
print(snack)

# Mutation
# add
numbers={10,20,30,40,50,60}
numbers.add(18)
print(numbers)

# update
numbers.update({25,35,45})
print(numbers)

# remove
numbers.remove(20)
print(numbers)

# discard method same as remove method

# Mathematical operations
# union
a={4,9,2,3,10,6}
b={4,5,6,9,7}
print(a.union(b))
print(a|b) # also performs union

#intersection
print(a.intersection(b))
print(a&b) # also performs intersection

#difference
print(a.difference(b))
print(a-b) # also performs difference

#symmetric difference
print(a.symmetric_difference(b))

#Iteration
companies={'Mclaren','Ferrari','Redbull','Mercedes','Haas'}
for comp in companies:
    print(comp)

#enumerate
for index,comp in enumerate(companies): #inside enumerate() u can specify start index, for ex: enumerate(companies,start=1)
    print(index,comp)