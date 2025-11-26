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

web = "https://pokeapi.co/api/v2/"

def get_pokemon(name):
    url = f"{web}pokemon/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        console.print("[bold red]❌ Noe gikk galt med API-kallet.[/bold red]")
        input("Trykk noe for å fortsette...")

def linje():
    console.print("[dim cyan]────────────────────────────────────────[/dim cyan]")

def vis_pokemon_kort(p: Pokemon_info, tittel="Pokémon"):
    """Full informasjon"""
    content = (
        f"[bold yellow]{p.name}[/bold yellow]\n"
        f"[cyan]Vekt:[/cyan] {p.weight} kg\n"
        f"[cyan]Høyde:[/cyan] {p.height} cm"
    )
    console.print(Panel(content, title=tittel, border_style="bright_magenta"))

def vis_skult_pokemon_kort(p: Pokemon_info):
    """Viser kun navn (for gjettefasen)"""
    content = (
        f"[bold yellow]{p.name}[/bold yellow]\n"
        f"[dim]???[/dim]"
    )
    console.print(Panel(content, title="Ny Pokémon", border_style="magenta"))


def main():
    ny_pokemon_get = get_pokemon(random.randint(1, 1025))
    gammel_pokemon = Pokemon_info(
        ny_pokemon_get['name'].title(),
        ny_pokemon_get['weight'] / 10,
        ny_pokemon_get["height"] * 10
    )

    score = 0

    console.print("\n[bold magenta]🎮 POKEMON HIGHER OR LOWER – VEKT[/bold magenta]\n")
    vis_pokemon_kort(gammel_pokemon, "Start Pokémon")

    while True:
        ny_pokemon_get = get_pokemon(random.randint(1, 1025))
        ny_pokemon = Pokemon_info(
            ny_pokemon_get['name'].title(),
            ny_pokemon_get['weight'] / 10,
            ny_pokemon_get["height"] * 10
        )

        linje()

        console.print(
            f"\n[bold white]⚖️  Veier[/bold white] [yellow]{gammel_pokemon.name} ({gammel_pokemon.weight} kg)[/yellow] "
            f"[bold white]mer enn[/bold white] [yellow]{ny_pokemon.name}?[/yellow]\n"
        )

        # 🔥 NY POKEMON VISER IKKE VEKT!
        vis_skult_pokemon_kort(ny_pokemon)

        console.print(f"[bold cyan]Score:[/bold cyan] [bold green]{score}[/bold green]\n")
        linje()

        while True:
            player_input = input("Y (Ja) eller N (Nei): ").lower()

            if player_input == "y":
                if gammel_pokemon.weight > ny_pokemon.weight:
                    console.print("[bold green]✔ Riktig![/bold green]")
                else:
                    console.print("[bold red]✘ Feil![/bold red]")

                console.print(f"[cyan]Riktig vekt:[/cyan] {ny_pokemon.weight} kg")

                if gammel_pokemon.weight > ny_pokemon.weight:
                    score += 1
                    input("Trykk en knapp... ")
                else:
                    console.print(f"[bold yellow]Final Score:[/bold yellow] {score}")
                    input("Trykk en knapp for å avslutte... ")
                    quit()

                break

            elif player_input == "n":
                if gammel_pokemon.weight <= ny_pokemon.weight:
                    console.print("[bold green]✔ Riktig![/bold green]")
                else:
                    console.print("[bold red]✘ Feil![/bold red]")

                console.print(f"[cyan]Riktig vekt:[/cyan] {ny_pokemon.weight} kg")

                if gammel_pokemon.weight <= ny_pokemon.weight:
                    score += 1
                    input("Trykk en knapp... ")
                else:
                    console.print(f"[bold yellow]Final Score:[/bold yellow] {score}")
                    input("Trykk en knapp for å avslutte... ")
                    quit()

                break

            else:
                console.print("[bold red]⚠ Skriv inn Y eller N[/bold red]")

        os.system("cls")
        gammel_pokemon = ny_pokemon

main()
