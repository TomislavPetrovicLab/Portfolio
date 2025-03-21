# format specifiers ={value:flags} format a value based on what flags are inserted

price1 = 3.14159
price2 = -98700.6535
price3 = 12454.3423

# print(f"Price 1 is ${price1:.3f}")   #to add a decimal point precision: .2f  (f is float. number)
# print(f"Price 2 is ${price2:.3f}")
# print(f"Price 3 is ${price3:.3f}")

# print(f"Price 1 is ${price1:10}")  # to display 10 spaces of the output
# print(f"Price 1 is ${price1:010}")   # to preceed output with 0 numbers add 0 before
# print(f"Price 1 is {price1:>10}")       # to justify to the right
# print(f"Price 1 is ${price1:<10}")      # to justify to the left
# print(f"Price 1 is ${price1:^10}")         # to align to the center
# print(f"Price 1 is ${price1:+}")        # to display plus infront of the positive values
# print(f"Price 1 is ${price1: }")         # to put space in front of the value
# print(f"Price 2 is ${price2:,}")            # for the values with 1,000.00
# print(f"Price 2 is ${price3:+,.2f}")         #combine multiple format specifiers
