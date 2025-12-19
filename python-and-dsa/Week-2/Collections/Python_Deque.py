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