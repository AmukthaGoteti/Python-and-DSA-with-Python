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
# We can also create Counter class object sing a list
# as an iterable data container
# import counter class from collection module
from collections import Counter
# Creating a counter class object usng list as an
# iterable data container
a = [12, 3, 4, 3, 5, 11, 12, 6, 7]
x = Counter(a)
# directly printing whole x
print(x)
# We can also use .key() and .values() methods to
# access Counter class object
for i in x.keys():
    print(i, ":", x[i])
# We can also make  list of keys and values of x
x_keys = list(x.keys())
x_values = list(x.values())
print(x_keys)
print(x_values)