# if = Do some code only IF some condition is True
#      Else do something else

# age = int(input("Enter your age: "))

# if age >= 100:
#     print("You are too old to sign up")
# elif age >= 18:
#     print("You are now signed up!")
# elif age < 0:
#     print("You haven't been born yet!")
# else:
#     print("You must be 18+ to sign up")

# It's important to know the order of conditions
# e.g., if the condition >= 100 was below >= 18, it would not be take into account
# if the input number is >= 18


# response = input("Would you like some food Y/N: ")

# if response == "Y":                   # for comparisons use double equal ==
#     print("Have some food!")
# else:
#     print("No food for you!")


# name = input("Enter your name: ")

# if name == "":
#     print("Error: You did not type in your name.")
# elif any(char.isdigit() for char in name):          #check if any character is digit in the name
#     print("Error: You typed in an invalid name format.")
# else:
#     print(f"Hello, {name}")


# for_sale = True

# if for_sale:                          # you can write condition or use booleans
#     print("This item is for sale")
# else:
#     print("This item is not for sale")


online = True

if online:
    print("The user is online")
else:
    print("The user is not online")