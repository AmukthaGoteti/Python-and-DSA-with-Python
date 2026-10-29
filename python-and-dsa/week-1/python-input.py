# Syntax: input(prompt)
# prompt is optional.
a = input("What colour is the rose? ")
print('The rose is', a)
# Taking input for other types of data
# Syntax: data_type(input(prompt)))
n = int(input("Enter an integer: "))
print('The integer is', n)
n = float(input("Enter a float: "))
print('The float is', n)
# Taking multiple inputs syntax: input(prompt).split()
x, y = input("Enter two numbers separated by space: ").split()
print("First number:", x)
print("Second number:", y)