import requests

web = "https://pokeapi.co/api/v2/"

def pokemon_get(name):
    
    url= f"{web}pokemon/{name}"
    response = requests.get(url)

    if response.status_code == 200:

        return response.json()
    else:
        print("Noe gikk galt")
        input("Trykk noe for å fortsette...")




