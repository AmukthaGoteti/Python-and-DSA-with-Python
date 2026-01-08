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
# Using int Default Factory
"""
    When the int class is passed as the default_factory argument, 
    then a defaultdict is created with default value as zero.
"""
from collections import defaultdict
d = defaultdict(int)
a = [1, 2, 3, 4, 2, 4, 1, 2]
for i in a:
    d[i] += 1
print(d)
# Using str Default Factory
"""
    With defaultdict(str), any new key automatically maps to '', 
    so you can concatenate text without key checks.
"""
from collections import defaultdict
# Uising str as the factory function
sd = defaultdict(str)
sd['greeting'] = 'Hello'
print(sd)
# Grouping Words by First Letter
"""
    defaultdict is very handy in text processing, 
    for example grouping words by their starting letter.
"""
from collections import defaultdict
words = ["apple", "ant", "banana", "bat", "carrot", "cat"]
grouped = defaultdict(list)
for word in words:
    grouped[word[0]].append(word)
print(grouped)
# Python defaultdict Type for Handling Missing Keys
"""
    Behind the scenes, defaultdict uses the 
    special __missing__() method:
    It is automatically called when a key is not found.
    If a default_factory is provided: its return value is used.
    If default_factory is None: a KeyError is raised.
"""
from collections import defaultdict
d = defaultdict(lambda: "Not Present")
d["a"] = 1
d["b"] = 2
print(d.__missing__('x'))
print(d.__missing__('d'))
print(d['a'])              # Normal access to existing key