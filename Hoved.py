import requests
import random
import os  

class Pokemon:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

# Makes a link to the api
web = "https://pokeapi.co/api/v2/"

def get_pokemon(name):
    
    # Gets info about the pokemon 
    url= f"{web}pokemon/{name}"
    response = requests.get(url)

    if response.status_code == 200:

        return response.json()
    else:
        print("Noe gikk galt")
        input("Trykk noe for å fortsette...")

def linje():
    print("-------------------------------------")

def main():
    ny_pokemon_get = random.randint(1, 1025)
    ny_pokemon_get = get_pokemon(ny_pokemon_get)
    gammel_pokemon = Pokemon(ny_pokemon_get['name'].title(), ny_pokemon_get['weight'] / 10)
    score = 0


    print(f"Navn: {gammel_pokemon.name}")
    print(f"Vekt: {gammel_pokemon.weight}kg")

    while True:
        ny_pokemon_get = random.randint(1, 1025)
        ny_pokemon_get = get_pokemon(ny_pokemon_get)

        
        linje()
        
        ny_pokemon_class = Pokemon(ny_pokemon_get['name'].title(), ny_pokemon_get['weight'] / 10)
        print(f"Veier {gammel_pokemon.name} ( {gammel_pokemon.weight} kg) mer en {ny_pokemon_class.name}? ")
        print(f"Navn: {ny_pokemon_class.name}")
        print(f"Score: {score}")


        linje()
        while True:
            player_input = input("Y or N: ").lower()
            if player_input == "y":
                if gammel_pokemon.weight > ny_pokemon_class.weight:
                    print("Det var riktig ")
                    print(f"Den veier {ny_pokemon_class.weight}")
                    score += 1
                    input("Trykk en knapp... ")
                else:
                    print("Det var feil ")
                    print(f"Den veier {ny_pokemon_class.weight}")
                    print(f"Scoren din ble: {score}")
                    input("Trykk en knapp å avslutte... ")
                    quit()
                break

            elif player_input == "n":
                if gammel_pokemon.weight <= ny_pokemon_class.weight:
                    print("Det var riktig ")
                    print(f"Den veier {ny_pokemon_class.weight}")
                    score += 1
                    input("Trykk en knapp... ")
                else:
                    print("Det var feil ")
                    print(f"Den veier {ny_pokemon_class.weight}")
                    print(f"Scoren din ble: {score}")
                    input("Trykk en knapp for å avslutte... ")
                    quit()
                break
            else:
                print("skriv inn Y eller N")
        # clears the terminal
        os.system("cls")
        gammel_pokemon = ny_pokemon_class

main()