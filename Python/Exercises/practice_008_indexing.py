# indexing = a method - accessing elements of a sequence using[] 9indexing (operator)
#            [start : end : step]

credit_number = "1234-5678-9012-3456"
# print(credit_number[4])         # it assumes you need the starting position
# print(credit_number[0 : 4])        # starting index is inclusive (includes the starting element)
                            # ending index is exclusive (excludes the ending index)
# print(credit_number[:4])    # it assumes that the starting position is 0 if not inputted
# print(credit_number[5 : 9])
# print(credit_number[5 :])       # to set to start from a certain position and till the end
# print(credit_number[-9])        # use negative numbers to start from the end reverse
# print(credit_number[::2])          # to print numbers in steps, e.g. every second


# EXERCISE: create a program that reads the last 4 digits of a credit card nubmer

# last_digits = credit_number[-4 :]
# print(f"XXXX-XXXX-XXXX-{last_digits}")

# EXERCISE: reverse all numbers
reverse_numbers = credit_number[::-1]
print(reverse_numbers)