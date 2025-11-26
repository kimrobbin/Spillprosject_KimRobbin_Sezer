import requests
import random
import os 
from pokemon import Pokemon
from rich import print
from rich.panel import Panel
from rich.console import Console

console = Console()

class Pokemon_info(Pokemon):
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
        print("[red]Noe gikk galt[/red]")
        input("Trykk noe for å fortsette...")

def linje():
    # Print a line separator
    print("[dim cyan]-------------------------------------[/dim cyan]")

def main():
    ny_pokemon_get = random.randint(1, 1025)
    ny_pokemon_get = get_pokemon(ny_pokemon_get)

    # Makes a object for gammel pokemon
    gammel_pokemon = Pokemon_info(ny_pokemon_get['name'].title(), ny_pokemon_get['weight'] / 10, ny_pokemon_get["height"] * 10)

    score = 0

    # Show first pokemon with a simple panel
    console.print(Panel(
        f"[bold yellow]{gammel_pokemon.name}[/bold yellow]\n"
        f"[cyan]Vekt:[/cyan] {gammel_pokemon.weight} kg\n"
        f"[cyan]Høyde:[/cyan] {gammel_pokemon.height} cm",
        title="Start Pokémon",
        border_style="magenta"
    ))

    while True:
        ny_pokemon_get = random.randint(1, 1025)
        ny_pokemon_get = get_pokemon(ny_pokemon_get)

        linje()

        # Makes a object for ny pokemon
        ny_pokemon = Pokemon_info(ny_pokemon_get['name'].title(), ny_pokemon_get['weight'] / 10, ny_pokemon_get["height"] * 10 )

        # Ask the question (no weight revealed on new Pokémon)
        print(f"[white]Veier[/white] [yellow]{gammel_pokemon.name} ({gammel_pokemon.weight} kg)[/yellow] "
              f"[white]mer enn[/white] [yellow]{ny_pokemon.name}[/yellow]?")

        # Show name only for new Pokémon
        console.print(Panel(
            f"[bold yellow]{ny_pokemon.name}[/bold yellow]\n[dim]???[/dim]",
            title="Ny Pokémon",
            border_style="magenta"
        ))

        print(f"[cyan]Score:[/cyan] [green]{score}[/green]")

        # Game Logic
        linje()
        while True:
            player_input = input("Y or N: ").lower()

            # Yes Logic
            if player_input == "y":
                # If gammel pokemon weights more then ny pokemon you get point 
                if gammel_pokemon.weight > ny_pokemon.weight:
                    print("[green]Det var riktig[/green]")
                    print(f"[cyan]Den veier:[/cyan] {ny_pokemon.weight}")
                    score += 1
                    input("Trykk en knapp... ")
                else:
                    print("[red]Det var feil[/red]")
                    print(f"[cyan]Den veier:[/cyan] {ny_pokemon.weight}")
                    print(f"[yellow]Scoren din ble:[/yellow] {score}")
                    input("Trykk en knapp å avslutte... ")
                    quit()
                break

            # No Logic
            elif player_input == "n":
                if gammel_pokemon.weight <= ny_pokemon.weight:
                    print("[green]Det var riktig[/green]")
                    print(f"[cyan]Den veier:[/cyan] {ny_pokemon.weight}")
                    score += 1
                    input("Trykk en knapp... ")
                else:
                    print("[red]Det var feil[/red]")
                    print(f"[cyan]Den veier:[/cyan] {ny_pokemon.weight}")
                    print(f"[yellow]Scoren din ble:[/yellow] {score}")
                    input("Trykk en knapp for å avslutte... ")
                    quit()
                break
            else:
                print("[red]skriv inn Y eller N[/red]")

        # Clears the terminal
        os.system("cls")
        gammel_pokemon = ny_pokemon

if __name__ == "__main__":
    main()
