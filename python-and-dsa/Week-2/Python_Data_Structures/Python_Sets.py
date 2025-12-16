# Python Sets
# Creating a set in Python
# Create a set of Integer Type
student_id = {112, 114, 116, 118, 115}
print('Student ID: ', student_id)
# Create a set of String Type
vowel_letters = {'a', 'e', 'i', 'o', 'u'}
print('Vowel Letters: ', vowel_letters)
# Create a set of Mixed Type
mixed_set = {'Hello', 101, -2, 'Bye'}
print('Set of mixed data types: ', mixed_set)
# When you run code that uses sets, the output may appear in different orders. This happens because a set does not maintain any specific or fixed order of its elements.
# Create an Empty Set in Python
# Create an empty set
empty_set = set()
# Create an empty dictionary
empty_dictionary = { }
# Check data type of empty_set
print('Data type of empty set: ', type(empty_set))
# check data type of dictionary_set
print('Data type of empty_dictionary:', type(empty_dictionary))
# Duplicate Items in a Set
numbers = {2, 4, 6, 6, 2, 8}
print(numbers)   # {8, 2, 4, 6}
# Adding and Updating Set Items in Python
# Add Items to a Set in Python
numbers = {21, 34, 54, 12}
print('Initial Set: ', numbers)
# Using add() method
numbers.add(32)
print('Updated Set: ', numbers)
# Update Python Set
companies = {'Lactose', 'Ralph Lauren'}
tech_companies = ['apple', 'google', 'apple']
# Using update() Method
companies.update(tech_companies)
print(companies)
# Output: {'apple', 'Ralph Lauren', 'Lactose', 'google'}
# Removing an Element from a Set
languages = {'Swift', 'Java', 'Python'}
print('Initial Set: ', languages)
# Remove 'Java' from the set
removedValue = languages.discard('Java')
print('Set after remove(): ', languages)
# Built-in Functions with Set
"""
    Function	    Description
    all()	        Returns True if all elements of the set are true (or if the set is empty).
    any()	        Returns True if any element of the set is true. If the set is empty, returns False.
    enumerate()	    Returns an enumerate object. It contains the index and value for all the items of the set as a pair.
    len()	        Returns the length (the number of items) in the set.
    max()	        Returns the largest item in the set.
    min()	        Returns the smallest item in the set.
    sorted()	    Returns a new sorted list from elements in the set(does not sort the set itself).
    sum()	        Returns the sum of all elements in the set.
"""
fruits = {"Apple", "Peach", "Mango"}
# for loop to access each fruits
for fruit in fruits:
    print(fruit)
# Finding Number of Set elements
even_numbers = {2, 4, 6, 8}
print("Set: ", even_numbers)
# Find number of elements
print("Total Elements: ", len(even_numbers))
# Python Set Operations
# Uinion of two sets
# first set
A = {1, 3, 5}
# Second set
B = {0, 2, 4}
# Perform union operationusing |
print("Union using |: ", A | B)
# Perform union operation using union()
print("union using union(): ", A.union(B))