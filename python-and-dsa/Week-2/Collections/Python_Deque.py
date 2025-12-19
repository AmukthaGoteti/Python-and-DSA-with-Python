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
# Count, Rotation and Reversal of a deque
from collections import deque
dq = deque([10, 20, 30, 40, 50, 20, 30, 20])
# 1. Counting occurrences of an element
count_20 = dq.count(20)
print("Count of 20:", count_20)
# 2. Rotating the deque
dq.rotate(2)  # Rotate right by 2
print("After rotating right by 2:", dq)
dq.rotate(-3)  # Rotate left by 3
print("After rotating left by 3:", dq)
# 3. Reversing the deque
dq.reverse()
print("After reversing the deque:", dq)