# **Ejercicios**

# Para estos ejercicios debe utilizar solo lo visto en clase. No es valido utilizar funciones como `zip` o `reversed`.**

# 1. Cree un programa que itere e imprima los valores de dos listas del mismo tamaño al mismo tiempo.}

cars_brands = ["Toyota", "BMW", "Ford", "RAM", "JEEP"]
models_cars = ["Hilux", "x6", "Raptor", "TRX", "WRANGLER"]

for car in range (min(len(cars_brands), len(models_cars))):
    print (cars_brands[car], models_cars[car])
    

# 1. Cree un programa que itere e imprima un string letra por letra de derecha a izquierda.
#     1. Pista: investigue de que otras maneras se puede usar el `range`.

my_car= "JEEP WRANGLER"

for car in my_car[::-1]:
    print (car)





my_country = " Costa Rica"

for i in range(len(my_country)-1,-1,-1):
    print (my_country[i])


# Cree un programa que intercambie el primer y ultimo elemento de una lista. Debe funcionar con listas de cualquier tamaño.

the_best_wwe_wrestlers= ["The Rock", "John Cena", "The Undertaker", " Rey Mysterio", "Randy Orton", "Shaw Micheles"]
for best in the_best_wwe_wrestlers[::-1]:
    print(best)

# Cree un programa que elimine todos los números impares de una lista

numbers = [1,2,3,4,5,6,7,8,9]
delete_numbers = []

for delete in range(len(numbers)-1, -1, -1):
    if numbers[delete] % 2 != 0:
        numbers.pop(delete)
        


print (f"The even numbers of the list are : {numbers} ")


# Cree un programa que le pida al usuario 10 números, y al final le muestre todos los números que ingresó, seguido del numero ingresado más alto.

numbers = []
higher = None
for i in range (10):
    number = int(input("Please, enter 10 numbers : "))

    numbers.append(number)

    if higher is None or number > higher:
        higher = number

print (f"The list are: {numbers} and the higher is: {higher}")


# 1. Cree un diccionario que guarde la siguiente información sobre un hotel:
#     - `nombre`
#     - `numero_de_estrellas`
#     - `habitaciones`
# - El value del key de `habitaciones` debe ser una lista, y cada habitación debe tener la siguiente información:
#     - `numero`
#     - `piso`
#     - `precio_por_noche`


hotel = {
    "name" : "Connor",
    "numbers_of_stars" : "5",
    "Rooms": [
        {
            "number": 100, "Floor" : 1, "night_price": 100,
            "number" : 101, "Floor": 5, "night_price": 150,
            "number" : 102, "Floor": 10, "night_price" : 300,

        }
    ]
}

print (hotel)

# Cree un programa que cree un diccionario usando dos listas del mismo tamaño, usando una para sus keys, y la otra para sus values

keys= ["ANIMAL", "CAR", "COUNTRY"]
values = ["SHARK", "DODGE", "ITALY"]

things = {}

for i in range(len(keys)):
    things[keys[i]]= values[i]


print ( things)


# Cree un programa que use una lista para eliminar keys de un diccionario.


soccer_teams = {
    "Real Madrid": "Spain",
    "All Nassar": "Saudit Arab",
    "Chelsea": "England",
    "Boca Juniors" : "Argentina",
    "Inter Miami": "USA",
}

remove_keys = ["Boca Juniors", "Inter Miami"]

for key in remove_keys:
    if key in soccer_teams:
        soccer_teams.pop(key)

print ( soccer_teams)


# Dada una lista de ventas con la siguiente información:
# date
# customer_email
# items
# Y cada item teniendo la siguiente información:
# name
# upc
# unit_price
# Cree un diccionario que guarde el total de ventas de cada UPC.


sales = [
    {
        "date": "01/03/2025",
        "customer_email" : "jeff@gmail.com",
        "items": [
            {
                "name": "Red Bull", "upc": "Dnks-181", "unit_price": 1.5,
            }
        ],
    },
    {
        "date": "15/03/2025",
        "customer_email" : "manolo@gmail.com",
        "items": [
            {
                "name": "Lays", "upc": "snks-171", "unit_price": 1,
            }
        ],  
    },

    {"date": "25/03/2025",
        "customer_email" : "tiapaola@gmail.com",
        "items": [
            {
                "name": "apple", "upc": "fruit-101", "unit_price": 1,
            }
        ],

    },
]

total_sales = {}

for sale in sales:
    for item in sale["items"]:
        upc = item ["upc"]
        price = item["unit_price"]


        if upc in total_sales:
            total_sales[upc] += price 
        else:
            total_sales[upc] = price


print (total_sales)


