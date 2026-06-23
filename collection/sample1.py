a=[1,2,3,4,5,6]
b=[44,55,66,77]
a[0] = 12 #list is mutable so we can change the value of element in list
a.pop(4) #pop() is used to remove element from list
a.insert(0,11) #insert() is used to insert element at specific position
print(a[2]) #a[] represents position of element in list
a.append(7)
a.append(67)
a.extend(b) #extend() is used to add elements of one list to another list
print(a)

#list