import requests
import random 

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



def main():
    ny_pokemon = random.randint(1, 1025)
    ny_pokemon = get_pokemon(ny_pokemon)
#    gammel_pokemon = ""

    print(f"Navn: {ny_pokemon['name'].title()}")
    print(f"Vekt: {ny_pokemon['weight']/10}kg")
#    print(f"Vekt: {gammel_pokemon['weight']/10}kg")


main()