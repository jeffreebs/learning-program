name = input("What is your name : ?")
fullname = input (" What is your fullname : ? ")
age = int(input ("How old are you : ? "))

if age < 1 : 
    print ( " You are a baby")
elif age > 1 and age < 12 :
    print ( " You are a child ")
elif age > 12 and age  < 15 :
    print (" You are a pre- teenager ")
elif age > 15 and age < 18 :
    print ( " You are a teenager ")
elif age >= 18 and age < 35 :
    print ( "Your a pre-adult ")
elif age > 35 and age < 65 :
    print ( " You are a adult ")
else:
    print ("You are a old person")