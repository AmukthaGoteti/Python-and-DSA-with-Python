# Python Deque
from collections import deque
# Declaring deque
de = deque(['name', 'age', 'DOB'])
print(de)
# Appending and Deleting Deque Items
de = deque([10, 20, 30])
# Add elements to the right
de.append(40)
print(de)
# Add elements to the left
de.appendleft(0)
print(de)
# Extend (Iterable)
de.extend([50, 60, 70])
print("After extend([50, 60, 70]): ", de)
# Extendleft (Iterable)
de.extendleft([-10, -20])
print("After extendleft([-10, -20]): ", de)
# Remove Method
de.remove(70)
print("After removing 70: ", de)
# Remove elements from the right
de.pop()
print("After pop(): ", de)
# Remove elements from the left
de.popleft()
print("After popleft(): ", de)
# Clear()
de.clear()
print("After clear(): ", de)
import collections
dq = collections.deque([1, 2, 3, 3, 4, 2, 4])
# Acessing elements by index
print(dq[0])
print(dq[-1])
# Finding the length of deque
print(len(dq))