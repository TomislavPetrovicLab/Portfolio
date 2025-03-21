# 2D lists = a list made of a lists; very flexible
#          = to make a grid or matrix of data -like.xls spreadsheet
#   you can create 2D tuples as well

# fruits =     ["apple", "orange", "banana", "coconut"]
# vegetables = ["celery", "carrots", "potatoes"]
# meat =       ["chicken", "fish", "turkey"]

# groceries = [fruits, vegetables, meat]

# or

groceries = [["apple", "orange", "banana", "coconut"],
             ["celery", "carrots", "potatoes"],
             ["chicken", "fish", "turkey"]]

print(groceries[0])         # returns entire indexed list
print(groceries[2][1])      # indexing elements in the 2D list;
# first index - row, second index - column


# Iterate over the elements in the 2D list - use nested loops:

for collection in groceries:      # iterates over the entire lists, not elements
    for food in collection:       # iterates over the elements in a list
        print(food, end=" ")
    print()

# 2D collection:
# Tuples in the lists
groceries = [("apple", "orange", "banana", "coconut"),
             ("celery", "carrots", "potatoes"),
             ("chicken", "fish", "turkey")]
# Tuples in tuples
# Sets in Tuples
    # depends on what you need

