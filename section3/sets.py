#definition - UNORDERED collections of UNIQUE elements 
my_set = set() #empty set
my_set2 = {1, 2, 3}
print(my_set2)

#adding element
my_set.add(1)
my_set.add(2)
print(my_set)

#elemets in sets are UNIQUE - no duplicates allowed
my_set.add(2)
    #no effect
print(my_set)

#casting a list to a set to get only the unique values:
my_list = [1,1,1,1,1,1,1,1,2,3,3,4,5,6,7,8,8,8]
print(set(my_list))

#string are lists of characters so we can get the unique
#values the same way
city = 'Mississippi'
print(city)
print(set(city))
