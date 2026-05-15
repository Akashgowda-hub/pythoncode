# Create an simple calculator

import os

os.system('cls' if os.name == 'nt' else 'clear')

var1 = int(input("Enter your first number = "))
var2 = int(input("Enter your Second number = "))

print ("Adding given two number output\n", var1 + var2)
print ("Subtract given two number output\n",var1 - var2)
print ("Multipling given two number output\n",var1 * var2)
print ("Division given two number output\n",var1 / var2)
print ("Radius given two number output\n",var1 // var2)
print ("Exponential given two number output\n",var1 ** var2)
print ("Percentage given two number output\n",var1 % var2)

input("Press Enter to clear...")

os.system('cls' if os.name == 'nt' else 'clear')