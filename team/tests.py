from rest_framework import status
from rest_framework.test import APITestCase

from team.models import Team
from trainer.models import Trainer


class TestTeamEndpoint(APITestCase):

    """
    Test Create and List APIs - Team
    """

    def setUp(self):
        self.trainer = Trainer.objects.create(name="Trainer", age=10, gender="M")

    def test_create_teams(self):
        try:
            response = self.client.post('/teams/', { "name" : "Team", "description": "Test team", "trainer": self.trainer.id}, format='json')

            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            self.assertEqual(Team.objects.count(), 1)
            self.assertEqual(Team.objects.get(id=1).name, 'Team')

        except Exception as e:
            raise Exception('Something went wrong: {}'.format(e))

    def test_get_teams(self):
        try:
            response = self.client.get('/teams/')

            self.assertEqual(response.status_code, status.HTTP_200_OK)

        except Exception as e:
            raise Exception('Something went wrong: {}'.format(e))