#create the empty list
my_list=[]
#append the element to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
#insert value on the second position
my_list.insert(2,15)
#extend the value on the List
my_list.extend([50,60,70])
#delete the last element
my_list.pop()
#Arranging the element in Ascending order
my_list.sort()


#Find and print the index of 30
index_30 = my_list.index(30)
print("Sorted List:", my_list)
print("Index of 30:", index_30)