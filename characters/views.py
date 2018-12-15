from rest_framework.viewsets import ModelViewSet

from . import models, serializers, filters


class CharacterViewSet(ModelViewSet):
    queryset = models.Character.objects.all()
    serializer_class = serializers.CharacterSerializer
    filterset_class = filters.CharacterFilterSet


class HeroViewSet(ModelViewSet):
    queryset = models.Hero.objects.all()
    serializer_class = serializers.HeroSerializer
    filterset_class = filters.HeroFilterSet


class SidekickViewSet(ModelViewSet):
    queryset = models.Sidekick.objects.all()
    serializer_class = serializers.SidekickSerializer
    filterset_class = filters.SidekickFilterSet


class VillainViewSet(ModelViewSet):
    queryset = models.Villain.objects.all()
    serializer_class = serializers.VillainSerializer
    filterset_class = filters.VillainFilterSet
