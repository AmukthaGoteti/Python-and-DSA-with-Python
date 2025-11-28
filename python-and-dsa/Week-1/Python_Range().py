# Print the numbers from 0 to 4
for i in range(5):
    print(i, end=" ")
print()
# Printing first 6
# whole numbers
for i in range(6):
    print(i, end=" ")
print()
# Printing a natural
# numbers from 5 to 20
for i in range(5, 20):
    print(i, end=" ")
print()
# Printing even numbers
for i in range(0, 10, 2):
    print(i, end=" ")
print()
# Increamented by 4
for i in range(0, 30, 4):
    print(i, end=" ")
print()
# incremented bt -2
for i in range(25, 2, -2):
    print(i, end=" ")
print()
from itertools import chain
# Using chain method
print("Concatenating the result")
res = chain(range(5), range(10, 20, 2))
for i in res:
    print(i, end=" ")
print()