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