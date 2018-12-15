from django_filters import rest_framework as filters

from . import models


class CharacterFilterSet(filters.FilterSet):

    class Meta:
        model = models.Character
        fields = {
            'name': ['exact', 'contains', 'icontains'],
        }


class HeroFilterSet(filters.FilterSet):

    class Meta:
        model = models.Hero
        fields = {
            'name': ['exact', 'contains', 'icontains'],
            'archenemy': ['exact'],
        }


class SidekickFilterSet(filters.FilterSet):

    class Meta:
        model = models.Sidekick
        fields = {
            'name': ['exact', 'contains', 'icontains'],
            'hero': ['exact'],
        }


class VillainFilterSet(filters.FilterSet):

    class Meta:
        model = models.Villain
        fields = {
            'name': ['exact', 'contains', 'icontains'],
            'archenemy': ['exact'],
        }
