# if Statement
num = int(input("Enter a number: "))
# check if the number is greater than 0
if num > 0:
    print(f'{num} is a positive number.')
print('A statement outside the if block.')
# indentation
x = 1
total = 0
# start of the if statement
if x!= 0:
    total += x
    print(total)
# end of the if statement
print("This is always executed.")
# if-else Statement
number = int(input("Enter a number: "))
if number > 0:
    print(f'{number} is a positive number.')
else:
    print(f'{number} is not a positive number.')
print('This statement always executes')
# if-elif-else Statement
number = -5
if number > 0:
    print(f'{number} is a positive number.')
elif number == 0:
    print('The number is zero.')
else:
    print(f'{number} is a negative number.')
print('This statement always executes.')
# nested if Statement
number = 5
# outer if statement
if number >= 0:
    # inner if statement
    if number == 0:
        print('The number is zero.')
    else:
        print(f'{number} is a positive number.')
else:
    print(f'{number} is a negative number.')
print('This statement always executes.')