# First match Case 

# variable = 10

# match variable:

#     case 10:
#         print (" Variable is Zero")
#     case _:
#         print ("variable")


# Second match Case

# age = int(input("Enter your Age :"))

# match age:

#     case x if (x >= 18):
#         print ("Your are eligible for vote")
#     case x if (x <= 17):
#         print ("Your are not eligible for vote")


# Third match Case

# Write a Python program using match-case that checks an order status.


# Use match-case to print:

# "Order delivered"
# → if status is "delivered"

# "Order shipped recently"
# → if status is "shipped" and days ≤ 3

# "Order shipped, delayed"
# → if status is "shipped" and days > 3

# "Order cancelled"
# → if status is "cancelled"

# "Unknown order status"
# → for everything else

status = ("delivered",100)

# match status:

#     case (x,y) if x == "shipped" and y <= 3:
#         print ("Order shipped recently")

#     case (x,y) if x == "delivered"and y = _:
#         print ("Order delivered")

#     case (x,y) if x == "shipped" and y > 3:
#         print ("Order shipped, delayed")

#     case (x,y) if x == "cancelled" and y _:
#         print ("Order cancelled")

#     case _:
#         print ("Unknown order status")

# Correct Logic 

match status:

    case ("shipped",y) if y <=3:
        print ("order shipped recently")

    case ("delivered",_):
        print ("order deliverd")

    case ("shipped",y) if y > 3:
        print ("Order shipped, delayed")
    
    case ("cancelled",_):
        print ("Order Cancelled")
    
    case _:
        print ("unknown order status")