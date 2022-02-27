from django.db import models

# Create your models here.
from team.models import Team


class Pokemon(models.Model):

    """
    Pokemon DB Model
    """

    name = models.CharField(max_length=255)
    nickname = models.TextField(max_length=255, null=True, blank=True)
    national_number = models.IntegerField(null=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):

        if self.team.pokemon_set.count() < 6:
            super(Pokemon, self).save()
        else:
            raise Exception(f'{self.team.name} is full!')

