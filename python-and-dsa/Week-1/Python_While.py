number = 1
while number <=3:
    print(number)
    number = number + 1
# Print numbers until the user enters 0
number = int(input("Enter a number: "))
# Iterate until the user enters 0
while number != 0:
    print(f'You entered {number}')
    number = int(input("Enter a number: "))
print('The End')