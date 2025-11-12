''' 
    Python Keywords define the rules and structure of Python programs, 
    which means you cannot use them as names for your variables, functions, classes, or any other identifiers. 
'''
# We can also get all the keyword names using the below
import keyword
# printing all keywords at once using "kwlist()"
print("The list of keywords is : ")
print(keyword.kwlist)
'''
    Output:
    The list of keywords is : 
    ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 
    'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 
    'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 
    'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
'''
'''
    We can identify a python Keyword by either with syntax hilighting where most IDEs provide syntax-highlight feature
    or look for syntax errors where this error will encounter if you have used any keyword incorrectly.
'''
# If we attempt to use a keyword as a variable, Python will raise a SyntaxError.
'''
    for = 10 
    print(for)
'''