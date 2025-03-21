# EXERCISE: countdown timer

import time

# time.sleep(3)       # sleep function - it displays message after 3 seconds

# print("TIME's UP!")

my_time = int(input("Enter the time in seconds: "))

# using reversed for reverse countdown
# for x in reversed(range(0, my_time)):
#     print(x)
#     time.sleep(1)

# print("WAKE UP!")


# or using steps by-1
for x in range(my_time, 0, -1):
    seconds = x % 60                # to avoid displaying 60
    minutes = int(x / 60 % 60)
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")    # display digital clock, use format sepcifier, use "0" padding
    time.sleep(1)

print("WAKE UP!")