import requests
import random
import os 
from pokemon import Pokemon

class Pokemon_Other_info(Pokemon):
    def __init__(self, name, weight, height):
        super().__init__(name, weight)
        self.height = height 
        
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

    # Makes a object for gammel pokemon
    gammel_pokemon = Pokemon(ny_pokemon_get['name'].title(), ny_pokemon_get['weight'] / 10)

    score = 0


    print(f"Navn: {gammel_pokemon.name}")
    print(f"Vekt: {gammel_pokemon.weight}kg")

    while True:
        ny_pokemon_get = random.randint(1, 1025)
        ny_pokemon_get = get_pokemon(ny_pokemon_get)

        
        linje()
         # Makes a object for ny pokemon
        ny_pokemon = Pokemon(ny_pokemon_get['name'].title(), ny_pokemon_get['weight'] / 10)
        print(f"Veier {gammel_pokemon.name} ( {gammel_pokemon.weight} kg) mer en {ny_pokemon.name}? ")
        print(f"Navn: {ny_pokemon.name}")
        print(f"Score: {score}")

        # Game Logic
        linje()
        while True:
            player_input = input("Y or N: ").lower()
            # Yes Logic
            if player_input == "y":
                # If gammel pokemon weights more then ny pokemon you get point 
                if gammel_pokemon.weight > ny_pokemon.weight:
                    print("Det var riktig ")
                    print(f"Den veier {ny_pokemon.weight}")
                    score += 1
                    input("Trykk en knapp... ")
                else:
                    print("Det var feil ")
                    print(f"Den veier {ny_pokemon.weight}")
                    print(f"Scoren din ble: {score}")
                    input("Trykk en knapp å avslutte... ")
                    quit()
                break
            # No Logic
            elif player_input == "n":
                if gammel_pokemon.weight <= ny_pokemon.weight:
                    print("Det var riktig ")
                    print(f"Den veier {ny_pokemon.weight}")
                    score += 1
                    input("Trykk en knapp... ")
                else:
                    print("Det var feil ")
                    print(f"Den veier {ny_pokemon.weight}")
                    print(f"Scoren din ble: {score}")
                    input("Trykk en knapp for å avslutte... ")
                    quit()
                break
            else:
                print("skriv inn Y eller N")

        # Clears the terminal
        os.system("cls")
        gammel_pokemon = ny_pokemon

main()