# Syntax for print() function in python
# Syntax: print(object(s), sep, end, file, flush)
# sep -> Seperartor
list = [1, 2, 3]
tuple = (1, 2, 3)
string = "Amuktha"
print(list, tuple, string)
# Syntax: print(*objects, sep=' ', end='\n', file=none, flush=False)
# *objects -> It can be one or more values to print
list = [1, 2, 3]
tuple = ("A", "B")
string = "Amuktha"
print(list, tuple, string, sep=" | ")
list = [1, 2, 3]
tuple = ("A", "B")
string = "Python"
print(list, tuple, string, end= " -> END\n")
# Syntax: f=open("file_name", "r")
f = open("python-and-dsa/week-1/geeksforgeeks.txt", "r")
print(f.read())
f.close()
import sys #sys -> system
company = "GeeksforGeeks"
loc = "Nodia"
mail = "contact@gfg.org"
print(company, loc, mail, file = sys.stderr) #sys.stderr -> system standard error
# Output Formatting Basic Syntax: "format-string" %value
# Syntax for multiple values: "format-string" %(value1, value2...)
print("Geeks: %2d, For: %5.2f" %(1, 05.333))
print("Total students: %3d, Boys: %2d" %(240, 120))
print("%7.3o" %(25))
print("%10.3E" %(356.08977))
# Positional Indexing Syntax: "{0} {1}", format(value1, value2)
print("I love {0} and \"{1}!\"" .format("Geeks", "Geeks"))
print(("{0} and Portal" .format("Geeks")))
print("Portal and {0}".format("Geeks"))
# Named arguments Syntax: "{variable_name}", format(variable_name=value)
template ="Number one portal is {0}, {1} and {other}."
print(template.format("Geeks", "for", other="Geeks"))
print("Geek: {0:2d}, Portal: {1:8.2f}" .format(12, 0.5534))