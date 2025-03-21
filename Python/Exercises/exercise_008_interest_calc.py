# Python compound interest calculator

principle = 0
interest = 0
time = 0

while True:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("The principle can not be less than 0.")
    else:
        break

while True:
    interest = float(input("Enter the interest amount: "))
    if interest < 0:
        print("The interest can not be less than 0.")
    else:
        break

while True:
    time = int(input("Enter the time in years: "))
    if time < 0:
        print("The time can not be less than 0.")
    else:
        break

total_balance = principle * pow((1 + interest / 100), time)
print(f"Your total balance: €{total_balance:,.2f}")