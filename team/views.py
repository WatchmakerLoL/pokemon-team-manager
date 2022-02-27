from rest_framework import viewsets

from team.models import Team
from team.serializers import TeamSerializer


class TeamViewset(viewsets.ModelViewSet):

    """
    API - Team Viewset for CRUD
    """

    serializer_class = TeamSerializer
    queryset = Team.objects.all()

    """
    TeamViewset urls:

    GET - teams/ - Retrieve all Team's Records
    POST - teams/ - Create a Team Record
    GET - teams/{id}/ - Retrieve a Team Record 
    DELETE - teams/{id}/ - Delete a Team Record
    PUT - teams/{id}/ - Update a Team Record
    PATCH - teams/{id}/ - Partially update a Team Record

    """

