# Practice Problem 1
# Hello World Program
print("Hello, World!") # Prints Hello, World!
print("""Hello
world""") # Prints Hello in first line and world in second line
# Practice Problem 2
# Learn to comment
class solution:
    def print_values(self, a, b, c):
        print(a, end=" ")
        # print(b, end=" ") # This line is commented out
        print(c, end=" \n")
solution = solution()
a, b, c = input().split()
solution.print_values(a, b, c)