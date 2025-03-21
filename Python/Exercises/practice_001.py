# this comment is important
#print("Obozavam gulas s njokima :)")
#print("It's really good!")

# Variable = A container (reusable) for a value (string, integer, float, boolean)
#            A variable behaves as if it was the value it contains

# Strings
#first_name = "Tom"
#food = "pizza"
#email = "myemail@domain.com"

# f-string
#print(f'Hello {first_name}')
#print(f"You like {food}")
#print(f"Your email is: {email}")


# Integers
#age = 25
#quantity = 7
#num_of_students = 95

#print(f"You are {age} years old")
#print(f'You are buying {quantity} items')
#print(f"Your class has {num_of_students} students")


# Floats - floating point number (number with decimal portion)
#price = 7.75
#gpa = 4.0
#distance = 3.4

#print(f"The price is {price}")
#print(f"Your gpa is: {gpa}")
#print(f"You ran {distance} km")


# Boolean - True or False
#is_student = True
#for_sale = True
#is_online = False

#print(f"Are you a student?: {is_student}")

#if is_online:
    #print(f"You are online")
#else:
    #print(f"You are offline")


# Typecasting - the process of converting a variable from one data type to another
#                str(), int(), float(), bool()

#name = "Tom"
#age = 40
#gpa = 4.1
#is_student = True

#gpa = int(gpa)
#print(gpa)

#age = float(age)
#print(age)

#age = str(age)

#print(age)
#print(type(age))

#age += "1"
#print(age)

#name = (bool(name))
#print(name)


# Input function
#name = input("What is your name?: ")
#number_of_pancakes = input("How many pancakes do you want?: ")

#print(f"You are {age} years old")

#age = input("How old are you?: ")
#age = int(age)
#age = age + 1

#print(f"Next year you'll be {age} old")
#print(f"Here are your {number_of_pancakes} pancakes, {name}. Enjoy!")

# better way:
age = int(input("How old are you?: "))
age = age + 1
print(f"Next year you'll be {age} years old")

