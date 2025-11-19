import requests
import random 

# Makes a link to the api
web = "https://pokeapi.co/api/v2/"

def pokemon_get(name):
    
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
    ny_pokemon = pokemon_get(ny_pokemon)
    gammel_pokemon = ny_pokemon

    print(f"Navn: {gammel_pokemon['name'].title()}")
    print(f"Vekt: {gammel_pokemon['weight']/10}kg")

    while True:
        ny_pokemon = random.randint(1, 1025)
        ny_pokemon = pokemon_get(ny_pokemon)

        
        linje()
        print(f"Veier {gammel_pokemon['name'].title()} mer en {ny_pokemon['name'].title()}?")
        print(f"Navn: {ny_pokemon['name'].title()}")

        player_input = input("Y or N")
        gammel_pokemon = ny_pokemon

main()