# Collections.UserDict in Python
"""
    An unordered collection of data values that are used to store data values like a 
    map is known as Dictionary in Python. 
    Unlike other Data Types that hold only a 
    single value as an element, Dictionary holds key:value pair. 
    Key-value is provided in the dictionary to make it more optimized.
"""
# Python program to demonstrate
# userdict
from collections import UserDict
d = {'a':1,
    'b': 2,
    'c': 3}
# Creating an UserDict
userD = UserDict(d)
print(userD.data)
# Creating an empty UserDict
userD = UserDict()
print(userD.data)
# Python program to demonstrate
# userdict
from collections import UserDict
# Creating a Dictionary where
# deletion is not allowed
class MyDict(UserDict):
    # Function to stop deletion
    # from dictionary
    def __del__(self):
        raise RuntimeError("Deletion not allowed")    
    # Function to stop pop from 
    # dictionary
    def pop(self, s = None):
        raise RuntimeError("Deletion not allowed")     
    # Function to stop popitem 
    # from Dictionary
    def popitem(self, s = None):
        raise RuntimeError("Deletion not allowed")
# Driver's code
d = MyDict({'a':1,
    'b': 2,
    'c': 3})
print("Original Dictionary")
print(d)
# d.pop(1)