#1
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"

print(thislist)


#2
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]

thislist[1:3] = ["blackcurrant", "watermelon"]

print(thislist)


#3
thislist = ["apple", "banana", "cherry"]

thislist[1:2] = ["blackcurrant", "watermelon"]

print(thislist)
#output: ['apple', 'blackcurrant', 'watermelon', 'cherry']


#4
thislist = ["apple", "banana", "cherry"]

thislist[1:3] = ["watermelon"]

print(thislist)
#output: ['apple', 'watermelon']


#5 insert item using (.insert)
thislist = ["apple", "banana", "cherry"]

thislist.insert(2, "watermelon")
#output:['apple', 'banana', 'watermelon', 'cherry']


print(thislist) 
