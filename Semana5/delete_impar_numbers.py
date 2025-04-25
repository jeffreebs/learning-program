numbers = [1,2,3,4,5,6,7,8,9]
delete_numbers = []

for delete in range(len(numbers)-1, -1, -1):
    if numbers[delete] % 2 != 0:
        numbers.pop(delete)
        


print (f"The even numbers of the list are : {numbers} ")