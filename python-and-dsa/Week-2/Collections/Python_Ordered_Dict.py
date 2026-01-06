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
# Insertion Order Preservation
"""
    OrderedDict maintains the sequence exactly as 
    elements were added. 
"""
from collections import OrderedDict
d = {'a': 1, 'b': 2, 'c': 3}
for k, v in d.items():
    print(k, v)
print('OrderedDict: ')
od = OrderedDict([('d', 4), ('b', 2), ('a', 1), ('c', 3)])
for k, v in od.items():
    print(k, v)
# Changing value does not affect order
"""
    In an OrderedDict, modifying the value of an 
    existing key does not change 
    its position in the order. 
    This means you can update the values 
    without affecting the original key order.
"""
from collections import OrderedDict
od = OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])
for k, v in od.items():
    print(k, v)
od['c'] = 5
for k, v in od.items():
    print(k, v)
# Equality checks consider order
"""
    Unlike regular dicts, orderedDic checks both content
    and order for equality, so differing orders make them
    unequal.
"""
from collections import OrderedDict
od1 = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
od2 = OrderedDict([('c', 3), ('b', 2), ('a', 1)])
print(od1 == od2)
# Reversing an OrderedDict
"""
    OrderedDict doesn't have a built-in reverse() method,
    but you can reverse its order 
    by using Python's reversed() 
    function on list(od.items()).
"""
from collections import OrderedDict
d1 = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
d2 = OrderedDict(reversed(list(d1.items())))
for k, v in d2.items():
    print(k, v)
# Pop Last or First Item
"""
    In OrderedDict, popitem() can remove either 
    the last item (last=True, default) or 
    the first item (last=False).
    In contrast, a normal dict’s popitem() 
    always removes the last item only.
"""
from collections import OrderedDict
d = OrderedDict([('a', 1), ('b', 2),('c', 3)])
res = d.popitem(last=True)
print(res)
# Move Keys to front or end
"""
    With the move_to_end() method, 
    OrderedDict provides the 
    flexibility to reposition keys.
"""
from collections import OrderedDict
d = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
d.move_to_end('a')
d.move_to_end('b', last=False)
for k, v in d.items():
    print(k, v)
# Deleting and re-inserting Keys
"""
    Deleting and re-inserting a key in an 
    OrderedDict moves it to the end, 
    preserving insertion order.
"""