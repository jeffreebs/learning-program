counter = 0
men_percentage = 0
women_percentage = 0
counter_women = 0
counter_men = 0
for counter in range (6) :
    info = int(input("Enter 1 for women or 2 for men :"))
    if info == 1:
        counter_women = counter_women + 1
    else:
        if info == 2:
            counter_men = counter_men + 1
        else: 
            print ( "Wrong´s number, please use 1 or 2 : ")
    counter = counter + 1
women_percentage = (counter_women / 6)*100
men_percentage = (men_percentage / 6) *100
print (f"The  men´s percentage are: {men_percentage}% and the women´s percentage are : {women_percentage}%")