from rest_framework.viewsets import ModelViewSet

from . import models, serializers, filters


class SecretIdentityViewSet(ModelViewSet):
    queryset = models.SecretIdentity.objects.all()
    serializer_class = serializers.SecretIdentitySerializer
    filterset_class = filters.SecretIdentityFilterSet


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
