# Function to print full pyramid pattern
def full_pyramid(n):
    for i in range(1, n + 1):
        # Print leading spaces
        for j in range(n - i):
            print(" ", end="")
        # Print Asterisks for the current row
        for k in range(1, 2 * i):
            print("*", end=" ")
        print()
full_pyramid(5)
# Full Pyramid Pattern in Python Recursion
def print_space(space):
    if space > 0:
        print(" ", end="")
        print_space(space - 1)
def print_star(star):
    if star > 0:
        print("*", end="")
        print_star(star - 1)
def print_pyramid(n, current_row = 1):
    if current_row > n:
        return
    spaces = n - current_row
    stars = 2 * current_row - 1
    # Print Spaces
    print_space(spaces)
    # Print Stars
    print_star(stars)
    # Move to next line for the next row
    print()
    # Print the pyramid for the next row
    print_pyramid(n, current_row + 1)
# Set the number of rows for the pyramid
n = int(input("Enter the number of rows for the pyramid: "))
# Print the pyramid pattern
print_pyramid(n)
# Pyramid Pattern in Python with Alphabet
n = 5
alph = 65
for i in range(0,n):
    print(" " * (n - i), end=" ")
    for j in range(0, i + 1):
        print(chr(alph + j), end=" ")
        alph += 1
    alph = 65
    print()
# Pyramid Patterns in Python with Numbers
def print_number_pyramid(rows):
    for i in range(1, rows + 1):
        # Print Spaces
        for j in range(rows - i):
            print(" ", end="")
        # Print Numbers
        for j in range(2 * i  - 1):
            print(j + 1, end="")
        # Move to the next line after each row
        print()
# Example usage
num_rows = int(input("Enter the number of rows for the number pyramid: "))
print_number_pyramid(num_rows)
# Function to print inverted full Pyramid pattern
def inverted_full_pyramid(n):
    # Outer loop for the number of rows
    for i in range(n, 0, -1):
        # Inner loop for leading spaces
        for j in range(n - i):
            print(" ", end="")
        # Inner loop for printing asterisks
        for k in range(2 * i - 1):
            print("*", end=" ")
        # Move to the next line after each row
        print()
# Set the number of rows for the inverted pyramid
n = int(input("Enter the number of rows for the inverted pyramid: "))
# Print the inverted pyramid pattern
inverted_full_pyramid(n)
def hallow_pyramid(n):
    for i in range(1, n + 1):
        for j in range(1, 2 * n):
            if j == n - i + 1 or j == n + i - 1 or i == n:
                print("*", end="")
            else:
                print(" ", end="")
        print()
# Set the number of rows for the hollow pyramid
n = int(input("Enter the number of rows for the hollow pyramid: "))
# Print the hollow pyramid pattern
hallow_pyramid(n)