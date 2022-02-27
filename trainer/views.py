from rest_framework import viewsets
from rest_framework.response import Response

from trainer.models import Trainer
from trainer.serializers import TrainerSerializer


class TrainerViewset(viewsets.ModelViewSet):
    """
    API - Trainer Viewset for CRUD
    """

    serializer_class = TrainerSerializer
    queryset = Trainer.objects.all()

    """
    TrainerViewset urls:
    
    GET - trainers/ - Retrieve all Trainer's Records
    POST - trainers/ - Create a Trainer Record
    GET - trainers/{id}/ - Retrieve a Trainer Record 
    DELETE - trainers/{id}/ - Delete a Trainer Record
    PUT - trainers/{id}/ - Update a Trainer Record
    PATCH - trainers/{id}/ - Partially update a Trainer Record

    """
