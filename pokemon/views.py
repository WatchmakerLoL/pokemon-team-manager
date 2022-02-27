from rest_framework import viewsets

from pokemon.models import Pokemon
from pokemon.serializers import PokemonSerializer
from pokemon.services import PokemonExternalAPI


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

    def perform_create(self, serializer):

        pokemon_eapi = PokemonExternalAPI()
        pokemon_data = pokemon_eapi.get_pokemon(serializer.data['name'])

        if pokemon_data:
            new_pokemon_data = {
                **serializer.data,
                "name": pokemon_data['name'],
                "national_number": pokemon_data['id']
            }

            serializer = PokemonSerializer(data=new_pokemon_data)

            if serializer.is_valid():
                serializer.create(validated_data=serializer.validated_data)
            else:
                raise Exception(f'Pokemon couldn\t be created')

