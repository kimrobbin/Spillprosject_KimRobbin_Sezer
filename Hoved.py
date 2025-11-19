import requests
import random
import os  


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
    gammel_pokemon = ny_pokemon

    print(f"Navn: {gammel_pokemon['name'].title()}")
    print(f"Vekt: {gammel_pokemon['weight']/10}kg")

    while True:
        ny_pokemon = random.randint(1, 1025)
        ny_pokemon = get_pokemon(ny_pokemon)

        
        linje()
        # Prints the new pokemon and ask about the old one
        print(f"Veier {gammel_pokemon['name'].title()} mer en {ny_pokemon['name'].title()}?")
        print(f"Navn: {ny_pokemon['name'].title()}")

        linje()
        player_input = input("Y or N: ")

        # clears the terminal
        os.system("cls")
        gammel_pokemon = ny_pokemon

main()