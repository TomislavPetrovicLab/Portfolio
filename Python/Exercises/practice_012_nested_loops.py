# nested loops = A loop within another loop (outer, iner)
#               outer loop:
#                   inner loop:

for x in range(3):          # print inner loop 3 times
    for y in range(1, 10):
        print(y, end="")    # to execute in the same line
    print()                 # to go to new line


# rectangle

rows = int(input("Enter the # of rows: "))
columns = int(input("Enter the # of columns: "))
symbol = input("Enter a symbol to use: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end = "")
    print()