#creating a list
my_list=[]
#appending numbers
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
#inserting a value specific position
my_list.insert(1,15)
#extend with anotherlist
my_list.extend([50,60,70])
# print(my_list)
#remove the last element
my_list.pop()
# print(my_list)
#sort in ascending order
my_list.sort()
# print(my_list)
#Find and print the index of the value 30 in my_list.
index_30 = my_list.index(30)
print(index_30)
print("final-list:",my_list)


