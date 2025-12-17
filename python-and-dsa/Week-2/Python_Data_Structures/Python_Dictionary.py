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