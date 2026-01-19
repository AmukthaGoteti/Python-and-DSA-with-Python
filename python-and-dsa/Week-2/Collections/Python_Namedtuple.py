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