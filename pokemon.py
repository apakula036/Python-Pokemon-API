import requests
import json

import tkinter as tk
from tkinter import filedialog, Text
import os 

from pokebase import cache, pokemon
cache.API_CACHE



def pokemonWeightandHeight():

    pokemonName = input("Enter Pokemon name:")
    print("You entered: " + pokemonName)


    pokemonData = requests.get('https://pokeapi.co/api/v2/pokemon/' + pokemonName)
    # print(pokemonData.json)
    pokemon = pokemonData.json()
    # print(pokemonData.status_code)
    print(pokemon['name'])
    print(str(pokemon['height']) + " " + str(pokemon['weight']))


root = tk.Tk()
canvas = tk.Canvas(root, height=700, width=700, bg="black")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

root.mainloop()