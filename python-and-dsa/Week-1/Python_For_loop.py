languages = ['Swift', 'Python', 'Go']
# Access elements of the list one by one
for lang in languages:
    print(lang)
Langauges = ['Swift', 'Python', 'Go']
# start of the loop
for lang in languages:
    print(lang)
    print('-----')
# end of the for loop
print('Last statement')
language = 'Python'
# Iterate over each character in the string
for x in language:
    print(x)
# Iterate over a range of numbers from 0 to 4
for i in range (0,4):
    print(i)
languages = ['Swift', 'Python', 'Go', 'C++']
for lang in languages:
    if lang == 'Go':
        break
    print(lang)
languages = ['Swift', 'Python', 'Go', 'C++']
for lang in languages:
    if lang == 'Go':
        continue
    print(lang)
# Outer Loop
attributes = ['Electric', 'Fast']
cars = ['Tesla', 'BMW', 'Audi']
for attribute in attributes:
    for car in cars:
        print(attribute, car)
    # This statement is outside the inner loop
    print('-----')
# iterate from i = 0 to 3
for _ in range(0, 4):
    print('Hi')