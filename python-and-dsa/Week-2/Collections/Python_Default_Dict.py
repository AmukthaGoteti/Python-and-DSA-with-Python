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