# Namedtuple in Python
"""
    In Python, NamedTuple is present inside the collections module.
    It provides a way to create simple, lightweight data structures 
    similar to a class, but without the overhead of defining 
    a full class. 
    Like dictionaries, they contain keys that are hashed to a 
    particular value.
    On the contrary, it supports both access 
    from key-value and iteration, 
    the functionality that dictionaries lack.

    Syntax:
        namedtuple(typename, field_names)
            typename - 
                The name of the namedtuple. 
            field_names - 
                The list of attributes stored in the namedtuple.
"""
# Python code to demonstrate namedtuple
from collections import namedtuple
# Declaring namedtuple
Student = namedtuple('Student', ['name', 'age', 'DOB'])
# Adding values
S = Student('Nandini', '19', '2541997')
# Accessing using index
print("The Student age using index is : ", end="")
print(S[1])
# Accessing using name
print("The Student name using keyname is : ", end="")
print(S.name)
# Create a NameTuple in Python
"""
    This creates a new namedtuple class using the namedtuple() function 
    from the collections module. 
    The first argument is the name of the new class, 
    and the second argument is a list of field names.
"""
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(x=1, y=2)
print(p.x, p.y)
# Access Operations
"""
    Namedtuples in Python provide convenient ways to access their fields. 
    Below are some access operations provided in Python for NamedTuple:
        Access by index
        Access by keyname
        Access Using getattr()
"""
# Access By Index
"""
    The attribute values of namedtuple() are 
    ordered and can be accessed using the index number 
    unlike dictionaries which are not accessible by index.
"""
# importing "collections" for namedtuple()
import collections
# Declaring namedtuple()
Student = collections.namedtuple('Student', ['name', 'age', 'DOB'])
# Adding values
S = Student('Nandini', '19', '2541997')
# Accessing using index
print("The Student age using index is : ", end="")
print(S[1])
# Access by keyname
# Access by keyname is also allowed as in dictionaries.
print("The Student name using keyname is : ", end="")
print(S.name)
# Access Using getattr()
"""
    This is yet another way to access the value by giving 
    namedtuple and key value as its argument.
"""
print("The Student DOB using getattr() is : ", end="")
print(getattr(S, 'DOB'))
# Conversion Operations
"""
    Namedtuples provide a few useful conversion 
    operations to work with other data types in Python. 
    Below are the following conversion operations 
    that is provided for namedtuples in Python:
        Using _make()
        Using _asdict()
        Using “**” (double star) operator
"""
# Using _make()
"""
    This function is used to return a namedtuple() 
    from the iterable passed as argument. 
"""
# importing "collections" for namedtuple()
import collections
# Declaring namedtuple()
Student = collections.namedtuple('Student', ['name', 'age', 'DOB'])
# Adding values
S = ['Nandini', '19', '2541997']
# initializing iterable
li = ["Manjeet", '19', '411997']
di = {'name': "Nikhil", 'age': 19, 'DOB': '1391997'}
# using _make() to return namedtuple()
print("The namedtuple instance using _make(): ")
print(Student._make(li))
# Conversion Operation Using _asdict()
"""
    This function returns the OrderedDict() 
    as constructed from the mapped values of namedtuple().
"""
import collections
# Declaring namedtuple()
Student = collections.namedtuple('Student', ['name', 'age', 'DOB'])
# Adding values
S = Student('Nandini', '19', '2541997')
# initializing iterable
li = ['Manjeet', '19', '411997']
# initializing dict
di = {'name': "Nikhil", 'age': 19, 'DOB': '1391997'}
# using _asdict() to return an OrderedDict()
print("The OrderedDict instance using namedtuple is  : ")
print(S._asdict())
# Using "**" (double star) operator
"""
    This function is used to convert a dictionary into the namedtuple().
"""
print("The namedtuple instance using ** operator is  : ")
print(Student(**di))
# Additional Operations
"""
    There are some additional operations 
    that are provided in Python 
    for NamedTuples:
        _fields
        _replace()
        __new__()
        __getnewargs__()
"""
# _fields
"""
    This data attribute is 
    used to get all the 
    keynames of the namespace declared.
"""
import collections
Student = collections.namedtuple('Student', ['name', 'age', 'DOB'])
# Adding Values
S = Student('Nandini', '19', '2541997')
# using _fields to print all the key names of namedtuple
print("The key names of namedtuple are : ")
print(S._fields)