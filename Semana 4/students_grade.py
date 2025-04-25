counter = 0
sum = 0
approved_grades = 0
disapproved_grades = 0
approved_average = 0
disapproved_average=0
total_average = 0

number_of_grades= int ( input ( "Enter the number of grades : "))
while counter < number_of_grades:
    actually_grade = int ( input ( f" Enter the actually student grade  # {counter + 1} "))
    counter = counter + 1
    if actually_grade  < 70 :
        disapproved_grades = disapproved_grades + 1
        disapproved_average = disapproved_average + actually_grade
    else:
        approved_grades = approved_grades + 1
        approved_average = approved_average + actually_grade

    total_average = total_average + actually_grade 

disapproved_average = disapproved_average / disapproved_grades if disapproved_grades > 0 else 0
approved_average = approved_average / approved_grades if approved_grades > 0 else 0
total_average = total_average / number_of_grades if number_of_grades > 0 else 0


print ( f" The student have this number of approved grades : {approved_grades}")
print ( f" The average of grade approved is : {approved_average}")
print(f"The student have this number of disapproved grades: {disapproved_grades}")
print(f"The average of grade approved is: {disapproved_average:.2f}")

print (f" This is the total average {total_average}")