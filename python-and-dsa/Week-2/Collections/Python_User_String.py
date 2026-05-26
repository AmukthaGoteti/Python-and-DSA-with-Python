# User String in Python
"""
    Python has something called UserString in the collections module.
    UserString is a way to create your own version of a string
    with additional or modified features.
"""
# Python program to demonstrate
# string
# Creating a String  
# with single Quotes 
String1 = 'Welcome to the Geeks World'
print("String with the use of Single Quotes: ") 
print(String1)
# Creating a String 
# with double Quotes 
String1 = "I'm a Geek"
print("\nString with the use of Double Quotes: ") 
print(String1)
# Python program to demonstrate
# userstring
from collections import UserString
d = 12344
# Creating an UserDict
userS = UserString(d)
print(userS.data)
# Creating an empty UserDict
userS = UserString("")
print(userS.data)