import requests
import json

class PokemonExternalAPI:
    """
    External Pokemon API Implementation.
    """
    base_api = 'https://pokeapi.co/api/v2/pokemon/'

    """
    Retrieve a Pokemon Record from an external API by Pokemon Name or Number.
    """
    def get_pokemon(self, value):
        r = requests.get('{}{}'.format(self.base_api, value))

        if r.status_code == 200:
            return json.loads(r.content.decode())
        else:
            raise Exception(f'{value} does not exist in PokemonDB.')