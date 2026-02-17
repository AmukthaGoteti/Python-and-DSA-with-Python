"""
    Python has something called UserList in the collections module. 
    UserList is a way to create your own version of a list with additional or modified features.
"""
# Python program to demonstrate
# Userlist
from collections import UserList
L = [1, 2, 3, 4]
# Creating a UserList
userL = UserList(L)
print(userL.data)