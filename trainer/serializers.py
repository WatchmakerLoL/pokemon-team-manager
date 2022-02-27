from rest_framework import serializers

from trainer.models import Trainer


class TrainerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trainer
        fields = '__all__'