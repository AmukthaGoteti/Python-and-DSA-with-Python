# User List in Python
"""
    Python has something called UserList in the collections module. 
    UserList is a way to create your own version of a list 
    with additional or modified features.
"""
# Python program to demonstrate
# Userlist
from collections import UserList
L = [1, 2, 3, 4]
# Creating a UserList
userL = UserList(L)
print(userL.data)
# Creating empty userlist
userL = UserList()
print(userL.data)
# Python program to demonstrate
# userlist
from collections import UserList
# Creating a List where
# deletion is not allowed
class MyList(UserList):
    # Function to stop deletion
    # from List
    def remove(self, s = None):
        raise RuntimeError("Deletion not allowed")
    # Function to stop pop from 
    # List
    def pop(self, s = None):
        raise RuntimeError("Deletion not allowed")
# Driver's code
L = MyList([1, 2, 3, 4])
print("Original List")
# Inserting to List"
L.append(5)
print("After Insertion")
print(L)
# Deleting From List
L.remove()