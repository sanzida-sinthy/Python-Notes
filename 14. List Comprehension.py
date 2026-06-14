# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
# Example:
# Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
# Without list comprehension you will have to write a for statement with a conditional test inside:


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
# output: ['apple', 'banana', 'mango']



# With list comprehension you can do all that with only one line of code:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)
# output: ['apple', 'banana', 'mango']


# Only accept items that are not "apple":
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
print(newlist)
# output: ['cherry', 'kiwi', 'banana', 'mango']



# With no if statement:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits]
print(newlist)
# output: ['apple', 'banana', 'cherry', 'kiwi', 'mango']

# You can use the range() function to create an iterable:
newlist = [x for x in range(10)]
print(newlist)
# output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


newlist = [x for x in range(10) if x < 5]
print(newlist)
# output: [0, 1, 2, 3, 4]

