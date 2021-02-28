import requests
import pandas as pd

endpoint = 'https://pokeapi.co/api/v2/pokemon/'

class Pokedex:
    def __init__(self):
        self.pokedex = []

    def get_entries(self):
        for num in range(1, 899):
            stats = requests.get(f'{endpoint}{num}').json()
            types = stats['types']
            if len(types) > 1:
                type = stats['types'][0]['type']['name'] + "/" + stats['types'][1]['type']['name']
                entry = {
                    'id': stats['id'],
                    'name': stats['name'],
                    "type": type,
                    'base_exp': stats['base_experience'],
                    'height': stats['height'],
                    'weight': stats['weight'],
                    'hp': stats['stats'][0]['base_stat'],
                    'attack': stats['stats'][1]['base_stat'],
                    'defense': stats['stats'][2]['base_stat'],
                    'special-attack': stats['stats'][3]['base_stat'],
                    'special-defense': stats['stats'][4]['base_stat'],
                    'speed': stats['stats'][5]['base_stat'],
                    'image': stats['sprites']['front_default']
                }
                self.pokedex.append(entry)
            else:
                type = stats['types'][0]['type']['name']
                entry = {
                    'id': stats['id'],
                    'name': stats['name'],
                    "type": type,
                    'base_exp': stats['base_experience'],
                    'height': stats['height'],
                    'weight': stats['weight'],
                    'hp': stats['stats'][0]['base_stat'],
                    'attack': stats['stats'][1]['base_stat'],
                    'defense': stats['stats'][2]['base_stat'],
                    'special-attack': stats['stats'][3]['base_stat'],
                    'special-defense': stats['stats'][4]['base_stat'],
                    'speed': stats['stats'][5]['base_stat'],
                    'image': stats['sprites']['front_default']
                }
                self.pokedex.append(entry)

        df = pd.DataFrame(self.pokedex)
        df.to_csv('pokedex_entries.csv', index=False)

