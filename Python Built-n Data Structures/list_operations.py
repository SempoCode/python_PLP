#List
my_list = []
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

print(my_list)

#inserting 15 at second position in my_list
my_list.insert(1, 15)

print(my_list)

#Extending my_list with another list
list1 =[50, 60, 70]
my_list.extend(list1)

print(my_list)

#removing the last element from my_list
del my_list[-1]

print(my_list)

#Sorting my_list in ascending order
my_list.sort(reverse = False)

print(my_list)

#finding and printing the index of the value 30 in my_list
print(my_list.index(30))
