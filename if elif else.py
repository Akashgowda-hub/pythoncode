passingcutoff = 35

English = int(input("Enter Your marks for English Subject : "))
Hindi = int(input("Enter Your marks for Hindi Subject : "))
Science = int(input("Enter Your marks for Science Subject : "))
Maths = int(input("Enter Your marks for Maths Subject : "))
Political = int(input("Enter Your marks for Political Subject : "))

total= English + Hindi + Science + Maths + Political
divtotal = total/500*100

if (divtotal < passingcutoff):
    print("Your percentages to low and your have failed the examination, Your percentange is" , (divtotal))
elif (divtotal ==  passingcutoff):
    print("Your have passes the examination, but tried to score well in upcoming examination. , Your percentange is" , (divtotal))
else:
    print("Your have passed the examination.Your percentange is" , (divtotal))