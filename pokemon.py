import requests
import json
from pokebase import cache, pokemon
cache.API_CACHE

pokemonName = input("Enter Pokemon name:")
print("You entered: " + pokemonName)


pokemonData = requests.get('https://pokeapi.co/api/v2/pokemon/' + pokemonName)
# print(pokemonData.json)
pokemon = pokemonData.json()
# print(pokemonData.status_code)
print(pokemon['name'])
print(str(pokemon['height']) + " " + str(pokemon['weight']))


