string1= "Hello "
string2 = " World "
print (string1 + string2)

string1 = " I´m "
int = 27
print (string1 + str(int))

days = 30
string1 = " days "
print (str(days) + string1)

days= [" monday " , " tuesday " , " wednesday " , " thursday " , " friday " , " saturday " , " sunday " ]
months = [" january " , " february " , " march " , " april " , " may " , " june " , " july ", " august " , " september " , " october " , " november " , " december "]
year = days + months
print (year)

string1 = " My family is made up of :  "
family = [" my brother " , " my  mom " , " my father "]
message = string1 + " , ".join(family)
print (message)   

num1 = 10
num2 = 10.5
result = num1 + num2
print (result)

bool1 = False
bool2 = False

print (bool1 + bool2)

bool1 = True
bool2 = False

print (bool1 + bool2)

bool1 = True
bool2 = True

print (bool1 + bool2)