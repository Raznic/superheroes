from rest_framework import serializers

from . import models


class CharacterSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Character
        fields = '__all__'


class HeroSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Hero
        fields = '__all__'


class SidekickSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Sidekick
        fields = '__all__'


class VillainSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Villain
        fields = '__all__'
