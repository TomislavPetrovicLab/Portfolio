# for loops = execute a block of code a fixed number of times
#             you can iterate over a range, strings, sequence, etc.

# count to 10:
# for x in range(1, 11):      # second number is exclusive
#    print(x)                # x is called counter

# for x in reversed(range(1, 11)):
#     print(x)
# print("HAPPY NEW YEAR!")

# for x in range(1, 11, 2):     # use steps, e.g. 2 steps
#     print(x)


# credit_card = "1234-5678-9012-3456"

# for x in credit_card:
#     print(x)

# to skip a number:
# for x in range(1, 21):
#     if x == 13:
#         continue
#     else:
#         print(x)

# to break at certain point use break:
for x in range(1, 21):
    if x == 13:
        break
    else:
        print(x)
