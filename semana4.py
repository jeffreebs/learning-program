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

#Cree un programa que le pida al usuario su nombre, apellido, y edad, y muestre si es un bebé, niño, preadolescente, adolescente, adulto joven, adulto, o adulto mayor.

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



#1. Cree un programa con un numero secreto del 1 al 10. El programa no debe cerrarse hasta que el usuario adivine el numero.
# 1. Debe investigar cómo generar un número aleatorio distinto cada vez que se ejecute.

import random

secret_number = random.randint(1 , 10)
number = int (input ( " Please, if you want to play, enter a number ( 1 - 10 ) : "))
counter = 0
while number != secret_number:
    print("Please, try again ...!")
    counter = counter + 1
    number = int (input ( " Please, try with another number : "))
print (f" Congratulations! you´ve guessed the secret number in {counter+1} opportunities ")

#Cree un programa que le pida tres números al usuario y muestre el mayor.

num1= int ( input ( " Enter the first number : "))
num2 = int (input ( " Enter the second number: "))
num3 = int (input ( " Enter the third number : "))

if num1 > num2 and num1 > num3:
    print (f"{num1} is th higher number ")
elif num2 > num1 and num2 > num3 :
    print (f"{num2} is th higher number")
else:
    print (f"{num3} is the higher number of the 3")


# 1. Dada `n` cantidad de notas de un estudiante, calcular:
#     1. Cuantas notas tiene aprobadas (mayor a 70).
#     2. Cuantas notas tiene desaprobadas (menor a 70).
#     3. El promedio de todas.
#     4. El promedio de las aprobadas.
#     5. El promedio de las desaprobadas.


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



# Ejercicios extra

# 1. Cree un pseudocódigo que le pida un `precio de producto` al usuario, calcule su descuento y muestre el precio final tomando en cuenta que:
#     1. Si el precio es menor a 100, el descuento es del 2%.
#     2. Si el precio es mayor o igual a 100, el descuento es del 10%.


product_price = int ( input ( " Enter please the product price :"))
if product_price < 100:
    discount_2 = product_price * 0.02
    total_price = product_price - discount_2
    print(f" Your discount is:  {discount_2}  and the total price is : {total_price}")
else:
    discount_10 = product_price * 0.10
    final_price = product_price - discount_10
    print (f" Your discount: {discount_10} and the total price is : {final_price} ")
    


# Cree un pseudocódigo que le pida un tiempo en segundos al usuario y calcule si es menor o mayor a 10 minutos. Si es menor,
# muestre cuantos segundos faltarían para llegar a 10 minutos. Si es mayor, muestre “Mayor”.

seconds_time = int (input ("Enter the seconds time : "))
if seconds_time < 600 :
    missing_time = 600 - seconds_time
    print (f" The time is less and missing :{missing_time} seconds")
else:
    print ( " Is higher ")

# Cree un algoritmo que le pida un numero al usuario, y realice una suma de cada numero del 1 hasta ese número ingresado.
# Luego muestre el resultado de la suma.


counter =1
sum = 0
num1= int(input("Enter the operations number that you want : "))
while counter <= num1 :
    sum = sum + counter
    counter = counter + 1
print (f"The sum result is : {sum}")

# Cree un algoritmo que le pida 2 números al usuario,
# los guarde en dos variables distintas (primero y segundo) y los ordene de menor a mayor en dichas variables.


num1 = int (input ("Enter the first number please : "))
num2 = int (input ("Enter the second number please  : "))
if num1 > num2:
    print (f" {num1} , {num2}")
else:
    print (f" {num2} , {num1}")


# Cree un algoritmo que le pida al usuario una velocidad en km/h y la convierta a m/s. Recuerda que 1 km == 1000m y 1 hora == 60 minutos * 60 segundos.

km_speed = float (input ("Enter the km speed : "))
meters_seconds = (km_speed * 1000) / 3600
print (f" The km speed is {meters_seconds} in meters/seconds")

# Cree un algoritmo que le pregunte al usuario por el sexo de 6 personas, ingresando 1 si es mujer o 2 si es hombre, 
# muestre al final el porcentaje de mujeres y hombres.

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


# Cree un diagrama de flujo que pida 3 números al usuario. 
# Si uno de esos números es 30, o si los 3 sumados dan 30, 
# mostrar “Correcto”. Sino, mostrar “incorrecto”.

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

# Cree un diagrama de flujo que le pida 5 números al usuario y muestre el mayor.

higher = int ()
for i in range (5) :
    num = int ( input ( "Enter a number to find out which one is higher  : "))
    if num > higher :
        higher = num 
print (f" The higher number is  : {higher}")


# Cree un diagrama de flujo que le pida un numero al usuario y muestre “Fizz” si es divisible entre 3, 
# “Buzz” si es divisible entre 5, y “FizzBuzz” si es divisible entre ambos.

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


# Cree un diagrama de flujo que le pida 100 números al usuario y muestre la suma de todos.


sum = 0
for i in range (100):
    num = int (input ("Enter a number : "))
    sum = sum + num
print(f"The result is : {sum}")

# Cree un diagrama de flujo que le pida 100 números al usuario y muestre el mayor de todos.



higher = int ()
for i in range (100):
    num = int (input ("Enter a number : "))
    if num > higher:
        higher = num
print(f"The higher number is : {higher}")