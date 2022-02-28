from rest_framework import viewsets
from rest_framework.response import Response

from pokemon.models import Pokemon
from pokemon.serializers import PokemonSerializer
from pokemon.services import PokemonExternalAPI

import json


class PokemonViewset(viewsets.ModelViewSet):

    """
    API - Pokemon Viewset for CRUD
    """

    serializer_class = PokemonSerializer
    queryset = Pokemon.objects.all()

    """
    PokemonViewset urls:

    GET - pokemons/ - Retrieve all Pokemon's Records
    POST - pokemons/ - Create a Pokemon Record
    GET - pokemons/{id}/ - Retrieve a Pokemon Record 
    DELETE - pokemons/{id}/ - Delete a Pokemon Record
    PUT - pokemons/{id}/ - Update a Pokemon Record
    PATCH - pokemons/{id}/ - Partially update a Pokemon Record

    """

    """
    Override default create to perform a request and get the pokemon data from the External API.
    """

    def create(self, request, *args, **kwargs):

        pokemon_eapi = PokemonExternalAPI()
        pokemon_data = pokemon_eapi.get_pokemon(request.data['name'])

        if pokemon_data:
            new_pokemon_data = {
                **request.data,
                "name": pokemon_data['name'],
                "nickname": request.data.get('nickname') if request.data.get('nickname', None) is not None
                                                            and request.data.get('nickname') != '' else pokemon_data['name'],
                "national_number": pokemon_data['id'],
                "type": ", ".join(typing.get('type').get('name', None) for typing in pokemon_data['types'])
            }

            serializer = PokemonSerializer(data=new_pokemon_data)

            try:
                if serializer.is_valid():
                    serializer.create(validated_data=serializer.validated_data)

                    return Response(serializer.data)
                else:
                    raise Exception(f'Pokemon couldn\t be created')
            except Exception as e:
                return Response({"error": str(e)})

