from django.db import models

from trainer.constants import POKEMON_TRAINER_GENDERS

class Trainer(models.Model):

    """
    Trainer DB Model
    """
    name = models.CharField(max_length=255, null=False, blank=False)
    age = models.IntegerField()
    gender = models.CharField(choices=POKEMON_TRAINER_GENDERS, max_length=1)

    def get_name(self):
        return self.name

    def __str__(self):
        return '{} - {} - {}'.format(self.get_name(), self.age, self.gender)
