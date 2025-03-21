# Logical operators = evaluate multiple conditions (or, and, not)
#                     or = at least one of the conditions is True
#                     and = all conditions must be True
#                     not = inverts the condition (not False, not True)

# temp = 0
# is_raining = True

# if temp > 35 or temp < 0 or is_raining:
#     print("The outdoor event is cancelled.")
# else:
#     print("The outdoor event is still scheduled.")


temp = -4
is_sunny = True

if temp < 0 and is_sunny:
    print("It is COLD outside. 🥶")
    print("It's SUNNY outside. 🌞")
elif 0 >= temp <= 28 and is_sunny:
    print("It is WARM outside. 😄")
    print("It's SUNNY outside. 🌞")
elif temp > 28 and not is_sunny:
    print("It is HOT outside. 🥵")
    print("It's CLOUDY outside. ☁️")
elif temp < 0 and not is_sunny:
    print("It is COLD outside. 🥶")
    print("It's SUNNY outside. ☁️")
elif 0 >= temp <= 28 and not is_sunny:
    print("It is WARM outside. 😄")
    print("It's SUNNY outside. ☁️")
elif temp > 28 and not is_sunny:
    print("It is HOT outside. 🥵")
    print("It's SUNNY outside. ☁️")

