from rest_framework import status
from rest_framework.test import APITestCase

from pokemon.models import Pokemon
from trainer.models import Trainer
from team.models import Team


class TestPokemonEndpoint(APITestCase):

    """
    Test Create and List APIs - Pokemon
    """

    def setUp(self):
        self.trainer = Trainer.objects.create(name="Trainer", age=10, gender="M")
        self.team = Team.objects.create(name="Team", description="description", trainer=self.trainer)

    def test_create_pokemons(self):
        try:
            response = self.client.post('/pokemons/', { "name" : 1, "team": self.team.id}, format='json')

            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            self.assertEqual(Pokemon.objects.count(), 1)
            self.assertEqual(Pokemon.objects.get(id=1).name, 'bulbasaur')

        except Exception as e:
            raise Exception('Something went wrong: {}'.format(e))

    def test_get_pokemons(self):
        try:
            response = self.client.get('/pokemons/')

            self.assertEqual(response.status_code, status.HTTP_200_OK)

        except Exception as e:
            raise Exception('Something went wrong: {}'.format(e))