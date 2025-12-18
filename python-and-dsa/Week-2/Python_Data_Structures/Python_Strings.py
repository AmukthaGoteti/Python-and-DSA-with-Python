# Python Strings
# Create a string using double quotes
string1 = "Python Programming"
print(string1)
# Create a string using single quotes
string1 = 'Python Programming'
print(string1)
# Create string type variable
name = "Python"
print(name)
message = "I love Python"
print(message)
# Access String Characters in Python
# Indexing
greet = 'Hello'
# Access 1st index element
print(greet[1])
# Negative Indexing
greet = 'Hello'
# Access 4th last element
print(greet[-4])
# Slicing
greet = 'Hello'
# Access character from 1st index to 3rd index
print(greet[1:4])
# Python Strings are immutable
""" 
    message = 'Hola Amigos'
    message[1] = 'H'
    print(message)
"""
message = 'Hola Amigos'
# Assign new string to message variable
message = 'Hello Friends'
print(message)
# Multiline String
message = """Never gonna give you up
Never gonna give you down"""
print(message)
# Python String Operations
# Compare Two Strings
str1 = "Hello, World!"
str2 = "I love swift"
str3 = "Hello, World!"
# compare str1 and str2
print(str1 == str2)
# compare str1 and str3
print(str1 == str3)
# Join Two or More Strings
greet = "Hello, "
name = "Jack"
# Using + operator
result = greet + name
print(result)
# Output: Hello, Jack
# Iterate trough a Python String
greet = 'Hello'
# iterate throudh greet
for letter in greet:
    print(letter)
# String membership test
print('a' in 'program')
print('at' not in 'battle')
# Python string Length
greet = "Hello"
# count length of greet string
print(len(greet))