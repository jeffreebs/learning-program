num1 = int ( input ( " Enter the first number : "))
num2 = int ( input ("Enter the second number : "))
num3 = int ( input("Enter the third number  : "))
suma = num1 + num2 + num3
if num1 == 30 or num2 == 30 or num3 == 30 :
    print ( "Correct")
elif suma == 30 :
    print ("Es correct")
else:
    print ("Incorrect")