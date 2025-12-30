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
# Elements on variety of counter objects with
# different data-containers
# import counter class from collections module
from collections import Counter
# Creation of a Counter Class Object using
# a string as an iterable data container
# Example - 1
a = Counter('GeeksforGeeks')
# Elements of Counter object
for i in a.elements():
    print(i, end=" ")
print()
# Example - 2
b = Counter({'geeks' : 4, 'for': 1, 'gfg' : 2,
             'python' : 3})
for i in b.elements():
    print(i, end=" ")
print()
# Example - 3
c = Counter([1, 2, 21, 12, 2, 44, 5, 13, 15, 5, 19,
             21, 5])
for i in c.elements():
    print(i, end =" ")
print()
# Example - 4
d = Counter(a = 2, b = 3, c = 6, d = 1, e = 5)
for i in d.elements():
    print(i, end =" ")
print()
# To demonstrate what elements() return when
# is printed directly
# import Counter from collections
from collections import Counter
# creating a raw data set
x = Counter("geeksforgeeks")
# Will return a iterable chain object
# which is basically a pseudo iterable container whose
# elements can be used when called wih iterable tool
print(x.elements())
# When the count of an item in Counter is initialised
# with negative values or zeros
# import Counter from collections
from collections import Counter
# creting a raw data-set using kewyword arguments
x = Counter(a = 2, x = 3, b = 3, z = 1, y = 5, c = 0, d = -3)
# printing out the lements
for i in x.elements():
    print("% s : % s" %(i, x[i]), end = "\n")