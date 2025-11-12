# Taking Input as a String
a = input("What color is the rose? ")
print("The rose is", a)
# Taking Input as an Integer
n = int(input("How many roses? "))
print("Total roses:", n)
# Taking Input as a Float
p = float(input("What is the price of one rose? "))
print("Price entered:", p)
# Taking Multiple Inputs
x, y = input("Enter two nos: ").split()
print("First no:", x)
print("Second no:", y)
# Name and Age Input
Name = input("Enter your name: ")
Age = input("Enter your age: ")
print("Name and Age: ", Name, Age)
# Adding Two Numbers
n1 = int(input("Enter first no: "))
n2 = int(input("Enter second no: "))
sum = n1 + n2
print("Sum is:", sum)
# Taking Lists as Input
a = list(input("List 1: "))
b = list(input("List 2: "))
for i in b:
    a.append(i)
print("Final List:", a)