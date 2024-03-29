from django.db import models

from trainer.models import Trainer

class Team(models.Model):

    """
    Team DB Model
    """

    name = models.CharField(max_length=255,blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, null=False)

    def get_name(self):
        return self.name

    def __str__(self):
        return '{} - owner: {}'.format(self.get_name(), self.trainer.get_name())

