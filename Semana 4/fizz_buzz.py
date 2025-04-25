num = int (input ( " Enter a number to find out what it can be divisible by : "))
if num % 5 == 0 and num % 3 == 0:
    print ("FizzBuzz")
elif num % 3 == 0 :
    print ("Fizz")
elif num % 5 == 0 :
    print ("Buzz")
elif num % 5 == 0 and num % 3 == 0:
    print ("FizzBuzz")
else:
    print ("Wrong")