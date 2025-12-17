# Python Dictionary
# Creating a dictionary
country_capitals = {
    "Germany" : "Berlin",
    "Canada" : "Ottawa",
    "England" : "London"
}
# Printing the dictionary
print(country_capitals)
# Access Dictionary Items
country_capitals = {
    "Germany" : "Berlin",
    "Canada" : "Ottawa",
    "England" : "London"
}
# Printing the values of keys
print(country_capitals["Germany"])
print(country_capitals["England"])
# Add items to a dictionary
country_capitals = {
    "Germany" : "Berlin",
    "Canada" : "Ottawa",
}
# Add an item with "Italy" as key and "Rome" as its value
country_capitals["Italy"] = "Rome"
print(country_capitals)
# Remove Dictionary Items
country_capitals = {
    "Germany" : "Berlin",
    "Canada" : "Ottawa"
}
# delete item having "Germany" key
del country_capitals["Germany"]
print(country_capitals)
country_capitals = {
    "Germany" : "Berlin",
    "Canada" : "Ottawa",
}
# Clear the dictionary
country_capitals.clear()
print(country_capitals)
# Change Dictionary Items
country_capitals = {
  "Germany": "Berlin", 
  "Italy": "Naples", 
  "England": "London"
}
# change the value of "Italy" key to "Rome"
country_capitals["Italy"] = "Rome"
print(country_capitals)
# Iterate Through a Dictionary
country_capitals = {
  "United States": "Washington D.C.", 
  "Italy": "Rome" 
}
# print dictionary keys one by one
for country in country_capitals:
    print(country)
print()
# print dictionary values one by one
for country in country_capitals:
    capital = country_capitals[country]
    print(capital)
# Find Dictionary Length
country_capitals = {"England": "London", "Italy": "Rome"}
# get dictionary's length
print(len(country_capitals))   # Output: 2
numbers = {10: "ten", 20: "twenty", 30: "thirty"}
# get dictionary's length
print(len(numbers))            # Output: 3
countries = {}
# get dictionary's length
print(len(countries))          # Output: 0
"""
    Function	    Description
    pop()	        Removes the item with the specified key.
    update()	    Adds or changes dictionary items.
    clear()	        Remove all the items from the dictionary.
    keys()	        Returns all the dictionary's keys.
    values()	    Returns all the dictionary's values.
    get()	        Returns the value of the specified key.
    popitem()	    Returns the last inserted key and value as a tuple.
    copy()	        Returns a copy of the dictionary.
"""