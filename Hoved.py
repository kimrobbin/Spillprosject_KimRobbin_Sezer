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
    ny_pokemon = random.randint(1, 1025)
    ny_pokemon = get_pokemon(ny_pokemon)
    gammel_pokemon = Pokemon(ny_pokemon['name'].title(), ny_pokemon['weight'] / 10)

    print(f"Navn: {gammel_pokemon.name}")
    print(f"Vekt: {gammel_pokemon.weight}kg")

    while True:
        ny_pokemon = random.randint(1, 1025)
        ny_pokemon = get_pokemon(ny_pokemon)

        
        linje()
        ny_pokemon_class = Pokemon(ny_pokemon['name'].title(), ny_pokemon['weight'] / 10)
        print(f"Veier {gammel_pokemon.name} mer en {ny_pokemon_class.name}? ")

        print(f"Navn: {ny_pokemon_class.name}")

        linje()
        player_input = input("Y or N: ")

        # clears the terminal
        os.system("cls")
        gammel_pokemon = ny_pokemon_class

main()