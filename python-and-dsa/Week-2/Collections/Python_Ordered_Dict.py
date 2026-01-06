# Python Ordered Dict
"""
    OrderedDict is a subclass of Python’s 
    built-in dictionary dict 
    that remembers the order in which keys are inserted.
"""
"""
    It provides extra powerful features, such as:
        1. Reordering keys dynamically with 
        move_to_end() (useful for FIFO/LIFO access).
        2. Popping items from 
        either end with popitem(last=True/False).
        3. Order-sensitive equality checks 
        (two OrderedDicts with same items 
        but different order are not equal).
        4. Easy implementation of data structures
        like queues, stacks, or LRU caches.
"""
from collections import OrderedDict
od = OrderedDict()
od['apple'] = 1
od['banana'] = 2
od['cherry'] = 3
print(list(od.items()))
"""
    Both OrderedDict and normal dict 
    preserve insertion order
    But only OrderedDict gives 
    advanced control over order
"""
from collections import OrderedDict
print("dict")
d={}
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
for key, val in d.items():
    print(key, val)
print('ordered dict')
od = OrderedDict()
od['d'] = 4
od['b'] = 2
od['a'] = 1
od['c'] = 3
for key, val in od.items():
    print(key, val)