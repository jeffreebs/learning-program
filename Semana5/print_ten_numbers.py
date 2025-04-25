numbers = []
higher = None
for i in range (10):
    number = int(input("Please, enter 10 numbers : "))

    numbers.append(number)

    if higher is None or number > higher:
        higher = number

print (f"The list are: {numbers} and the higher is: {higher}")