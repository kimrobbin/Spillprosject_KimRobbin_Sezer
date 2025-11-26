from pokemon import Pokemon
from Hoved import Pokemon_info
import pytest

def test_pokemon():
    poke = Pokemon('Bulbasaur', 6.9)
    assert poke.name == 'Bulbasaur'
    assert poke.weight == 6.9

def test_pokemon_info():
    poke = Pokemon_info('Charmander', 8.5, 60)
    assert poke.name == 'Charmander'
    assert poke.weight == 8.5
    assert poke.height == 60

def test_pokemon_info():
    poke = Pokemon_info('Squirtle', 9.0, 50)
    assert isinstance(poke, Pokemon)


