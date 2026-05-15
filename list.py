# pic1 = input("Enter the First movie name: ")
# pic2 = input("Enter the Second movie name: ")
# pic3 = input("Enter the Third movie name: ")

# list = [pic1, pic2, pic3]

# print(list)

lit = [1,2,3,4,3,2,1]
lit.copy()
newlit = print(lit)

lit.reverse()
revlit= print(lit)

if newlit == revlit:
    print("This is palindrome")
else:
    print("Not an palindrome")
