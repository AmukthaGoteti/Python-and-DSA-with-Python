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