from rest_framework import status
from rest_framework.test import APITestCase

from trainer.models import Trainer


class TestTrainerEndpoint(APITestCase):

    """
    Test Create and List APIs - Trainer
    """

    def test_create_trainers(self):
        try:
            response = self.client.post('/trainers/', { "name" : "Trainer", "age": 10, "gender": "M"}, format='json')

            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            self.assertEqual(Trainer.objects.count(), 1)
            self.assertEqual(Trainer.objects.get(id=1).name, 'Trainer')

        except Exception as e:
            raise Exception('Something went wrong: {}'.format(e))

    def test_get_trainers(self):
        try:
            response = self.client.get('/trainers/')

            self.assertEqual(response.status_code, status.HTTP_200_OK)

        except Exception as e:
            raise Exception('Something went wrong: {}'.format(e))



