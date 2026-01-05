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