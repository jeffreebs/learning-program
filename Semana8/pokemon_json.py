import json

def add_pokemon ():
    try:
        with open ("pokemons.json", "r",) as file:
            pokemons = json.load(file)
    except FileNotFoundError:
        pokemons = []

    print ("We will come to add a new pokemon : ")
    name = input ("Enter the name of the pokemon : ")
    t_ype = input ("Enter the type of the pokemon : ")
    hp= int ( input (" Enter th HP of the pokemon : "))
    attack = int ( input ( " Enter the attack of the pokemon : "))
    defense = int (input("Enter the defender of the pokemon : "))
    sp_attack= int (input("Enter the SP. Attack of the pokemon : "))
    sp_defense = int ( input ( " Enter the Sp. defense of the pokemon : "))
    velocity = int (input ("Enter the velocity of the pokemon : "))


    new_pokemon={
        "name":{
            "english": name
        },
        "type": t_ype,
        "base":{
            "HP": hp,
            "Attack": attack,
            "Defense": defense,
            "Sp. Attack": sp_attack,
            "Sp. Defense": sp_defense,
            "Speed": velocity
            
        }

    }

    pokemons.append(new_pokemon)

    with open ("pokemons.json", "w",)as file:
        json.dump(pokemons,file,indent=4)

    print (f"The pokemon {name} has been added successfully ")

if __name__ == "__main__":
    add_pokemon()