#Please explain what it means that a list is mutable and a string is not mutable (imutable).
#Give some code that shows the difference.

# A list is mutable, meaning that it can be changed after it is created.
# A string is immutable, thereby it cannot be changed after it is created.
# The next code will display the difference between the two:

list = [10, 20, 30, 40, 50] #creating a list
print(list) #printing the list
list[1] = 60 #changing the first element of the list
print(list) #printing the list

string = "Dana" #creating a string
print(string) #printing the string
string[0] = "J" #trying to change the first letter of the string
print(string) #printing the string, but it will display an error message, because strings are immutable


