from rest_framework.viewsets import ModelViewSet

from . import models, serializers


class CharacterViewSet(ModelViewSet):
    queryset = models.Character.objects.all()
    serializer_class = serializers.CharacterSerializer


class HeroViewSet(ModelViewSet):
    queryset = models.Hero.objects.all()
    serializer_class = serializers.HeroSerializer


class SidekickViewSet(ModelViewSet):
    queryset = models.Sidekick.objects.all()
    serializer_class = serializers.SidekickSerializer


class VillainViewSet(ModelViewSet):
    queryset = models.Villain.objects.all()
    serializer_class = serializers.VillainSerializer
