import random

secret_number = random.randint(1 , 10)
number = int (input ( " Please, if you want to play, enter a number ( 1 - 10 ) : "))
counter = 0
while number != secret_number:
    print("Please, try again ...!")
    counter = counter + 1
    number = int (input ( " Please, try with another number : "))
print (f" Congratulations! you´ve guessed the secret number in {counter+1} opportunities ")
