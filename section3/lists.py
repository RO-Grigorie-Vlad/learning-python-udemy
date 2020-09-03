#definition:
my_list = [1, 2, 3]

#lists can have elemets of more than one type
my_list2 = ["String", 100, 23.2]
print(my_list)
print(my_list2) 

#list elements can be acessed by index
print(my_list[0])

#lists can be concaternated 
print(my_list + my_list2)

#lists are mutable
my_list[0] = 4
print(my_list)

#adding an element to the end of the list
my_list.append(5)
print(my_list)

#remove element from the end of the list + and print it
my_list.pop()
print(my_list)

#remove element from a certain index
my_list.pop(0)
print(my_list)

#sort - sorts a list - doesnt return anything
my_list = [3, 2, 1, 5, 4]
my_list.sort()
print(my_list)

#reverse - doesnt return anything
my_list.reverse()
print(my_list)