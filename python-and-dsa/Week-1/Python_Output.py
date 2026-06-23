# Python print() function
# print() function is used to print a python object(s) in python as standard output
# Syntax -> print(object(s), sep, end, file, flush)
# Eample 1
# Sample Python Objects
list = [1, 2, 3]
tuple = ("A", "B")
string = "Amuktha"
# Printing the objects
print(list, tuple, string)
"""
    Syntax:
        print(*objects, sep=' ', end='\n', file=None, flush=False)
    
    Parameters:

        *objects: one or more values to print (positional arguments)
        sep: string inserted between objects (default is ' ')
        end: string appended at the end (default is '\n')
        file: output stream (default is sys.stdout)
        flush: whether to flush the stream immediately 
        (default is False)
    
    Note: 
        The parameters sep, end, file, and flush in the print() 
        function are keyword-only arguments. 
        This means they must be specified using their 
        parameter names, not by position.
"""

# Example 2
# Sample python objects
list = [1, 2, 3,]
tuple = ("A", "B")
string = "Amuktha"
# Printing the Objects
print(list, tuple, string, sep = " | ")

# Example 3
# sample python objects
list = [1,2,3]
tuple = ("A","B")
string = "Python"
# printing the objects
print(list,tuple,string, end=" --> END\n")

# Example 4
# Open and read the file
f = open("python-and-dsa/Week-1/geeksforgeeks.txt","r")
# Print the contents of the file
print(f.read())
f.close()

# Example 5
# Python code for printing to stderr
# importing the package
# for sys.stderr
import sys 
# variables
Company = "Geeksforgeeks.org"
Location = "Noida"
Email = "contact@geeksforgeeks.org"
# print to stderr
print(Company, Location, Email, file=sys.stderr)

# Python - Output Formatting
# string modulo operator(%)
print("Geeks : %2d, Portal : %5.2f" % (1, 05.333)) 
print("Total students : %3d, Boys : %2d" % (240, 120))   # print integer value
print("%7.3o" % (25))   # print octal value
print("%10.3E" % (356.08977))   # print exponential value

# Positional formatting with format() method
# Using indexed placeholders for string formatting
print("I love {0} for \"{1}!\"".format("Geeks", "Geeks"))
# {0} is replaced by the first argument 'Geeks'
print("{0} and Portal".format("Geeks"))
# Formatting with placeholders, {0} replaced by 'Geeks'
print("Portal and {0}".format("Geeks"))

# Advanced formatting with positional and named arguments
# Mutliple placeholders
name = "Geeks"
age = 3
print("Name: {}, Age: {}".format(name, age))
# Mixing positional and named arguments
template = "Number one portal is {0}, {1} and {other}."
print(template.format("Geeks", "For", other="Geeks"))
# Format integers and floats with specified width and precision
print("Geeks :{0:2d}, Portal :{1:8.2f}".format(12, 0.5534))
# Demonstrate order swapping and formatting precision
print("Second argument: {1:3d}, first one: {0:8.2f}".format(47.42, 11))
# Using named arguments for clarity in complex formats
print("Geeks: {a:5d}, Portal: {p:8.2f}".format(a=453, p=59.058))

cstr = "I love geeksforgeeks"
# Printing the center aligned string with fillchr
print("Center aligned: ")
print(cstr.center(40, '#'))
# Printing the left aligned string with "-" padding
print("left aligned: ")
print(cstr.ljust(40, '-'))
# Printing the right aligned string with "-" padding
print("right aligned: ")
print(cstr.rjust(40, '-'))