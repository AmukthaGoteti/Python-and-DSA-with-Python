# Python - Counter Objecs - elements()
# Working of elements() on a simple data container
# import counter class from collections modle
from collections import Counter
# Creating of a COunter Class object using
# string as iterable data container
x = Counter("geeksforgeeks")
# printing the elements of counter object
for i in x.elements():
    print(i, end= " ")
print()