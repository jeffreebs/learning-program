# Cree dos funciones que impriman dos cosas distintas, y haga que la primera llame la segunda.

def sum_the_number():
    num1=10
    num2=20
    result = num1 + num2
    print (f"The result is : {result}")


    rest_the_number()



def rest_the_number ():
    num1 = int(input("Please, enter the first number: "))
    num2= int(input("Please enter the second number: "))
    result = num1 - num2
    print(f"The rest of the 2 numbers is: {result}")



sum_the_number()


# 1. Experimente con el concepto de scope:
#     1. Intente accesar a una variable definida dentro de una función desde afuera.
#     2.  Intente accesar a una variable global desde una función y cambiar su valor.

# def print_variable():
#     print(f'Inside function: {variable_outside_function_scope}')


# print_variable()
# print(f'Outside function: {variable_outside_function_scope}')



# def my_dream_car():
#     my_car = "JEEP"
#     print (my_car)


# print(my_car)


my_dream_cars = ["Toyota", "Ford", "BMW", "Nissan"]

def add_brand():
    my_dream_cars.append("Baic")
    my_dream_cars.append("Suzuki")
    my_dream_cars.append("Mazda")
    print (my_dream_cars)

def deleted_car():
    my_dream_cars.pop(1)
    my_dream_cars.pop(3)
    print(my_dream_cars)

def duplicated_car():
    duplicated = my_dream_cars * 2
    for car in duplicated:
        print (car)

def main():
    add_brand()
    deleted_car()
    duplicated_car()

main()

# 1. Cree una función que retorne la suma de todos los números de una lista.
#     1. La función va a tener un parámetro (la lista) y retornar un numero (la suma de todos sus elementos).
#     2. [4, 6, 2, 29] → 41



def return_the_numbers(number = [10,20,30,40,50]):
    sumatory = sum(number)
    print (f"The sum of the list is: {sumatory} ")
    number = [10,20,30,40,50]
return_the_numbers()


# 1. Cree una función que le de la vuelta a un string y lo retorne.
#     1. Esto ya lo hicimos en iterables.
#     2. “Hola mundo” → “odnum aloH”

def reversed_string ():
    string = "Hello my friend"
    result = string[::-1]
    print (result)
reversed_string()

# Cree una función que imprima el numero de mayúsculas y el numero de minúsculas en un string.

def print_letters(strings):
    upper= 0
    lower = 0

    for letter in strings:
        if letter.isupper():
            upper+=1
        elif letter.islower():
            lower += 1
    print (f"The text have : {upper} upper letters")
    print (f"The text have : {lower} lower letters")

print_letters("Hello world from python")

# 1. Cree una función que acepte un string con palabras separadas por un guión y retorne un string igual pero ordenado alfabéticamente.
#     1. Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.
#     2. “python-variable-funcion-computadora-monitor” → “computadora-funcion-monitor-python-variable”

def order_strings(string):
    string_list = string.split("-")

    string_list_order = sorted(string_list)

    result = "-".join(string_list_order)

    return result

input_string = input("Enter some words to order the list: ")
output_strings= order_strings(input_string)

print(output_strings)


# 1. Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.
#     1. [1, 4, 6, 7, 13, 9, 67] → [7, 13, 67]
#     2. Tip 1: Investigue la logica matematica para averiguar si un numero es primo, y conviertala a codigo. No busque el codigo, eso no ayudaria.
#     3. *Tip 2: Aquí hay que hacer varias cosas (recorrer la lista, revisar si cada numero es primo, y agregarlo a otra lista). Así que lo mejor es agregar **otra función** para revisar si el numero es primo o no.*

def prime_number (num):
    if num <= 1:
        return False
    

    for n in range(2,int(num ** 0.5)+1):
        if num % n == 0:
            return False
    return True

def get_primes (list):
    prime= []
    for number in list:
        if prime_number(number):
            prime.append(number)
    return prime

def main():
    list1 = [1,4,6,7,13,9,67]
    prime = get_primes(list1)
    print(f"Prime numbers:{prime}")

main()


