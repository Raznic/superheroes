from rest_framework import serializers

from . import models


class SecretIdentitySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.SecretIdentity
        fields = '__all__'


class HeroSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Hero
        exclude = ['secret_identity']

    secret_identity_id = serializers.PrimaryKeyRelatedField(
        queryset=models.SecretIdentity.objects.all(),
        allow_null=True,
        required=False,
        source='secret_identity'
    )
    secret_identity_url = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='v1:secretidentity-detail',
        source='secret_identity'
    )
    sidekick_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True,
        source='sidekicks'
    )
    sidekick_urls = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='v1:sidekick-detail',
        source='sidekicks'
    )
    archenemy_id = serializers.PrimaryKeyRelatedField(
        queryset=models.Villain.objects.all(),
        allow_null=True,
        required=False,
        source='archenemy'
    )
    archenemy_url = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='v1:villain-detail',
        source='archenemy'
    )


class SidekickSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Sidekick
        exclude = ['secret_identity', 'hero']

    hero_id = serializers.PrimaryKeyRelatedField(
        queryset=models.Hero.objects.all(),
        source='hero'
    )
    hero_url = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='v1:hero-detail',
        source='hero'
    )
    secret_identity_id = serializers.PrimaryKeyRelatedField(
        queryset=models.SecretIdentity.objects.all(),
        allow_null=True,
        source='secret_identity'
    )
    secret_identity_url = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='v1:secretidentity-detail',
        source='secret_identity'
    )


class VillainSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Villain
        exclude = ['archenemy']

    archenemy_id = serializers.PrimaryKeyRelatedField(
        queryset=models.Hero.objects.all(),
        allow_null=True,
        source='archenemy'
    )
    archenemy_url = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='v1:hero-detail',
        source='archenemy'
    )
