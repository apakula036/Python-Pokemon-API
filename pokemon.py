import requests
import json
from pokebase import cache, pokemon
cache.API_CACHE

pokemonData = requests.get('https://pokeapi.co/api/v2/pokemon/gloom')

print(pokemonData.status_code)
