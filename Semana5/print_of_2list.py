cars_brands = ["Toyota", "BMW", "Ford", "RAM", "JEEP"]
models_cars = ["Hilux", "x6", "Raptor", "TRX", "WRANGLER"]

for car in range (min(len(cars_brands), len(models_cars))):
    print (cars_brands[car], models_cars[car])