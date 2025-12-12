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