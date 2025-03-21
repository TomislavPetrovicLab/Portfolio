# WHILE loop = will execute some code WHILE some condition is true
#              very useful for verifying user input


# EXAMPLE 1

# name = input("Enter your name: ")

# if name == "":
#    print("You didn't specify your username.")
# else:
#     print(f"Hello, {name}")

# if condition is not true, it exits the while loop
# while name == "":              # checks whether the name is empty ""
#     print("You didn't specify your name.")
#     name = input("Enter your name: ")       # without this row it's infinte loop, you need exit strategy
# print(f"Hello, {name}")


# EXAMPLE 2

# age = int(input("Enter your age: "))

# while age < 0:
#     print("Age can't be negative number")
#     age = int(input("Enter your age: "))

# print(f"You are {age} years old.")


# EXAMPLE 3: use "not" logical operator

# food = input("Enter the food you like (or press q to quit): ")

# while not food == "q":
#     print(f"You like {food}.")
#     food = input("Enter another food you like (or press q to quit): ")

# print("Ok, bye!")


# EXAMPLE 4: use "or" logical operator

num = int(input("Enter a number between 1 - 10: "))

while num <1 or num > 10:
    print(f"{num} is not a valid number")
    num = int(input("Enter a number between 1 - 10: "))

print(f"You picked number {num}.")