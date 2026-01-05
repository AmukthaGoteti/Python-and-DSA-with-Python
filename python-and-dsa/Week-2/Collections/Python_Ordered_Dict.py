# Python Ordered Dict
"""
    OrderedDict is a subclass of Python’s 
    built-in dictionary dict 
    that remembers the order in which keys are inserted.
"""
from collections import OrderedDict
od = OrderedDict()
od['apple'] = 1
od['banana'] = 2
od['cherry'] = 3
print(list(od.items()))