# Defaultdict in Python
"""
    In Python, defaultdict is a subclass of 
    the built-in dict class from the collections module. 
    It automatically assigns a default value to keys 
    that do not exist, which means you don’t have to 
    manually check for missing keys and avoid KeyError.
"""
from collections import defaultdict
d = defaultdict(list)
d['fruits'].append('apple')
d['vegetables'].append('carrot')
print(d)
print(d['juices'])
# Syntax -> defaultdict(default_Factory)
"""
    default_factory: A callable (like int, list, set, str or 
    a custom function) that provides the default value for 
    missing keys.
    If this argument is None, 
    accessing a missing key raises a KeyError.

    Returnn Value: It returns a dictionary that 
    gives a default value when a key is missing, 
    instead of showing an error.
"""
# UUse Case of defaultdict
# Using List as Default Factory
"""
    When the list class is passed as the default_factory argument, 
    then a defaultdict is created with the values that are list.
"""
from collections import defaultdict
d = defaultdict(list)
for i in range(5):
    d[i].append(i)
print("Dictionary with values as list: ")
print(d)