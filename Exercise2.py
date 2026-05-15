import time

timestamp = int(time.strftime ('%H'))

# abcd = "21"

# timestamp = int(abcd)

print(timestamp)

if (timestamp <= 11):
    print ("Good Morning")
elif (timestamp <= 16):
    print ("Good Afternoon")
elif (timestamp <= 20):
    print ("Good Evening")
else:
    print ("Good Night")