# Python Lists
# Create a list
# A list of 3 elements
ages = [19, 29, 29]
print(ages)
# List Items of Different Types
# A list containing strings, numbers and another list
student = ['Jack', 32, 'Computer Science', [2, 4]]
print(student)
# An empty List
empty_list = []
print(empty_list)
# Accessing List Items
languages = ['Python', 'Swift', 'C++']
# Access the 1st element
print("Languages[0]: ",languages[0])
# Access the 3rd element
print("Languages[2]: ",languages[2])
# Negative Indexing
languages = ['Python', 'Swift', 'C++']
# Access the last element
print("Languages[-1]: ",languages[-1])
# Access the third last element
print("Languages[-3]: ",languages[-3])
# Slicing a List
my_list = ['p', 'r', 'o', 'g', 'r', 'a', 'm']
print("my_list = ", my_list)
# elements from index 2 to index 4
print("my_list[2:5] = ", my_list[2:5])
# elements from index 2 to index -3
print("my_list[2:-3] = ", my_list[2:-2])
# elements from the beginning to index 2
print("my_list[0:3] = ", my_list[0:3])
# Omiting Start and ending Indices in slicing
my_list = ['p', 'r', 'o', 'g', 'r', 'a', 'm']
# get a list with items from index 5 to last
print("my_list[5:] = ", my_list[5:])
# get a list from the first item toindex -5
print("my_list[:-4] = ", my_list[:-4])
# ommiting both start and end index
# get a list from start to end items
print("my_list[:] = ", my_list[:])
# Add Elements to a List
# Using append() to add an element to the end of the list
fruits = ['Apple', 'Banana', 'Orange']
print("Original List: ", fruits)
fruits.append('Cherry')
print("Updated List: ", fruits)
# Add an element at a specific position using insert()
fruits = ['Apple', 'Banana', 'Orange']
print("Original List: ", fruits)
fruits.insert(2, 'Cherry')
print("Updated List: ", fruits)
# Add multiple elements to a list using extend()
numbers = [1, 3, 5]
print("Number: ", numbers)
even_numbers = [2, 4, 6]
print("Even Numbers: ", even_numbers)
# adding elements of one list to another
numbers.extend(even_numbers)
print("Updated Numbers: ", numbers)
# Changing List Items
colors = ['Red', 'Black', 'Green']
print("Original List: ", colors)
# change the 1st item to 'purple'
colors[0] = 'Purple'
# change the third item to 'blue'
colors[2] = 'Blue'
print("Updated List: ", colors)
# Removing List Items
# Using remove() to remove a specific item
numbers = [2, 4, 7, 9]
# remove 4 from the list
numbers.remove(4)
print(numbers)
names = ['John', 'Eva', 'Nick', 'Jack']
# delete the item at index 1
del names[1]
print(names)
# delete items from index 1 to index 2
del names[1:3]
print(names)
# delete the entire list
del names
# Error! List doesn't exist
# print(names) -> Will raise an error
# Python List Length
cars = ['BMW', 'Mercedes', 'Tesla']
print("Number of cars: ", len(cars))
# Iteratin through the list
fruits = ['Apple', 'Banana', 'Orange']
for fruit in fruits:
    print(fruit)
"""
    Method	    Description
    append()	Adds an item to the end of the list
    extend()	Adds items of lists and other iterables to the end of the list
    insert()	Inserts an item at the specified index
    remove()	Removes the specified value from the list
    pop()	    Returns and removes item present at the given index
    clear()	    Removes all items from the list
    index()	    Returns the index of the first matched item
    count()	    Returns the count of the specified item in the list
    sort()	    Sorts the list in ascending/descending order
    reverse()	Reverses the item of the list
    copy()	    Returns the shallow copy of the list
"""