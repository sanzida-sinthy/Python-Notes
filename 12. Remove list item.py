thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
#output: ['apple', 'cherry']


#If there are more than one item with the specified value, the remove() method removes the first occurrence:
#Example
#Remove the first occurrence of "banana":

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)
#output: ['apple', 'cherry', 'banana', 'kiwi']


#Remove the second item:
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
#output: ['apple', 'cherry']


# Remove the last item:
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
# output: ['apple', 'banana']


# Remove the first item:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
 # output:["banana", "cherry"]


# Delete the entire list:
thislist = ["apple", "banana", "cherry"]
del thislist
print(thislist) #this will cause an error because you have succsesfully deleted "thislist".



# The clear() method empties the list.
# The list still remains, but it has no content.

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
