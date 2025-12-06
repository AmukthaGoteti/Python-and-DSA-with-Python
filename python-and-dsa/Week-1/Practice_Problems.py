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
# Practice Problem 3
# The New Line
class solution:
    def new_line(self):
        print("Geeks\nfor\nGeeks")
solution = solution()
solution.new_line()
# Practice Problem 4
# Leap Year
class Solution:
    def checkYear(self, n):
        if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0):
            return True
        else:
            return False
n = int(input())
solution = Solution()
if (solution.checkYear(n)):
    print("True")
else:
    print("False")