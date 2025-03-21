# Collection = single "variable" used to store multiple values
#   List = [] ordered and changeable. Duplicates OK
#   Set = {} unordered and immutable, but Add/Remove OK. NO duplicates
#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER


# LISTS:
# fruits = ["apple", "orange", "banana", "coconut"]

# print(fruits)
# print(fruits[4])    # indexing - to return particular values/elements in a list
# print(fruits[:3])    # list first 3 elements
# print(fruits[::-1])    # list backwards entire list

# Iterate collections with the "for" loop:
# for fruit in fruits:
#     print(fruit)

# List all methods that can be used with lists:
# print(dir(fruits))
# Description of each listed function:
# print(help(fruits))

# number of elements in list:
# print(len(fruits))

# check if value is in the collection with "in":
# print("pineapple" in  fruits)

# to change a value(element) in the list:
# fruits[0] = "pineapple"
# print(fruits[0])

# for fruit in fruits:
#     print(fruit)

# Methods for lists:
#   to append (add) an element to the list:

# fruits.append("pinepple")
# print(fruits)

# To remove ana element:
# fruits.remove("apple")
# print(fruits)

# Insert a value at a given index:
# fruits.insert(0, "pineapple")
# print(fruits)

# Sort elements in alphabetical order:
# fruits.sort()
# print(fruits)

# To reverse the order of the elements:
# fruits.reverse()
# print(fruits)

# To clear the list:
# fruits.clear()
# print(fruits)

# Return the index of a value from the list:
# print(fruits.index("coconut"))

# To count the number of times the same value is found in the list:
# fruits.append("banana")
# print(fruits.count("banana"))
# print(fruits.count("pineapple"))


# SETS - they don't return the same order of values when printed
#      - they work well if you work with constants or colors e.g.:

# fruits = {"apple", "orange", "banana", "coconut"}
# print(fruits)
# print(dir(fruits))
# print(help(fruits))

# print("pineapple" in fruits)

# Cannot use indexing on sets because they are unordered:
# print(fruits[0])  # ERROR

# fruits.add("pineapple")
# fruits.remove("apple")
# print(fruits)

# To remove first element that pops out:
# fruits.pop()
# print(fruits)

# To clear all values in the set:
# fruits.clear()
# print(fruits)


# TUPLE:

fruits = ("apple", "banana", "orange", "coconut", "apple")
# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("pineapple" in fruits)

# print(fruits.index("apple"))      # find a value in a tuple
# print(fruits.count("apple"))      # count a number of same value in tuples

# for fruit in fruits:
#     print(fruit)