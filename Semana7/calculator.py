
print( " Welcome to the calculator ")

def main():
    result = 0
    first_operation = True


    while True:

        print("------Welcome to the calculator Menu ------")
        print("Please, enter a number to choose an option ")
        print("----- 1.Sum")
        print("------2.Rest")
        print("------3.Multiply")
        print("------4.Div")
        print("------5.To leave the calculator")
        print("------6.Clear the result")
        print(f"The current result is : {result}")


        


        option = int(input("Please, enter a number (1-5) to choose an option : "))

        if option == 1:
                try:
                    if first_operation:
                        num1 = int(input("Enter the first number to sum: "))
                        num2 = int(input("Enter the second number to sum: "))
                        result = num1 + num2  
                        first_operation = False 
                    else:
                        num = int(input("Enter a number to add: "))
                        result += num  
                    print(f"The result of the operation is: {result}")
                    
                except ValueError:
                    print("You need to enter a valid number please")


        elif option == 2:
                try:


                    if first_operation:
                        num1 = int(input("Enter the first number to subtract: "))
                        num2 = int(input("Enter the second number to subtract: "))
                        result = num1 - num2  
                        first_operation = False 
                    else:
                        num = int(input("Enter a number to subtract: "))
                        result -= num  
                    print(f"The result of the operation is: {result}")

                except ValueError:
                    print("You need to enter a valid number please")

        elif option == 3:
                try:
                    

                    if first_operation:
                        num1 = int(input("Enter the first number to multiply: "))
                        num2 = int(input("Enter the second number to multiply: "))
                        result = num1 * num2  
                        first_operation = False  
                    else:
                        num = int(input("Enter a number to multiply: "))
                        result *= num 
                        print(f"The result of the operation is: {result}")

                except ValueError:
                    print("You need to enter a valid number please")

        elif option == 4:
                try:

                    if first_operation:
                        num1 = int(input("Enter the first number to divide: "))
                        num2 = int(input("Enter the second number to divide: "))
                        if num2 == 0:
                            raise ZeroDivisionError("You can't divide by zero!")
                            result = num1 / num2  
                            first_operation = False  
                    else:
                        num = int(input("Enter a number to divide: "))
                        if num == 0:
                            raise ZeroDivisionError("You can't divide by zero!")
                            result /= num  
                            print(f"The result of the operation is: {result}")
                    
                except ZeroDivisionError as ex:
                    print (ex)
                except ValueError:
                    print("You need to enter a valid number  ")
        elif option == 5:
                print("Thanks for visit the calculator")
                break
        elif option == 6:
                result = 0
                first_operation = True
                print ( "The result has been reset ")
        else:
                print ( "Error, please choose a valid option ")

        

if __name__ == "__main__":
    main ()


