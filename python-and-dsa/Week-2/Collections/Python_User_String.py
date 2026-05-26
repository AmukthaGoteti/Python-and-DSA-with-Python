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
String1 = 'Welcome to the geeksforgeeks'
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
# Python program to demonstrate
# userstring
from collections import UserString
# Creating a Mutable String
class Mystring(UserString):
    # Function to append to
    # string
    def append(self, s):
        self.data += s   
    # Function to remove from 
    # string
    def remove(self, s):
        self.data = self.data.replace(s, "") 
# Driver's code
s1 = Mystring("Geeks")
print("Original String:", s1.data)
# Appending to string
s1.append("s")
print("String After Appending:", s1.data)
# Removing from string
s1.remove("e")
print("String after Removing:", s1.data)