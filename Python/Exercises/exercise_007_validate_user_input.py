# Exercise: Validate user input
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 4. username must not contain digits

username = input("Enter your username: ")


if len(username) > 12:
    print("Error: Your username can not contain more than 12 characters.")
elif not username.find(" ") == -1:
    print("Error: Your username can not contain any spaces.")
elif not username.isalpha():
    print("Error: Your username can not contain any digits.")
else:
    print(f"Welcome, {username}!")