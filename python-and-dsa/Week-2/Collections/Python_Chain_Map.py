# ChainMap in Python
"""
    Python contains a container called chainMap which encapsulates
    many dictionaries into one unit. ChainMap is memeber of module
    collections
"""
# Python program to demonstrate
# ChainMap
from collections import ChainMap
d1 = {'a' : 1, 'b' : 2}
d2 = {'c' : 3, 'd': 4}
d3 = {'e': 5, 'f' : 6}
# Defining the chainmap
c = ChainMap(d1, d2, d3)
print(c)
# Access Operations
"""
    keys() :- This function is used to display all the keys of all the dictionaries in ChainMap.
    values() :- This function is used to display values of all the dictionaries in ChainMap.
    maps() :- This function is used to display keys with corresponding values of all the dictionaries in ChainMap.
"""
# Please select Python 3 for running this code in IDE
# Python code to demonstrate ChinMap and
# keys(), values() and maps
# importinf collections for ChainMap operations
import collections
# Initializing dictionaries
dic1 = {'a' : 1, 'b' : 2}
dic2 = {'b' : 3, 'c' : 4}
# Initializing ChainMap
chain = collections.ChainMap(dic1, dic2)
# printing ChainMap using maps
print("All the ChainMap contents are: ")
print(chain.maps)
# printing keys using keys()
print("All the keys of ChainMap are: ")
print(list(chain.keys()))
# printing keys using keys()
print("All values of ChainMap are: ")
print(list(chain.values()))