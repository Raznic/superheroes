import uuid
from django.db import models


class SecretIdentity(models.Model):

    id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        primary_key=True
    )
    name = models.CharField(
        max_length=100,
        blank=False
    )


class Hero(models.Model):

    id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        primary_key=True
    )
    name = models.CharField(
        max_length=100,
        blank=False
    )
    secret_identity = models.OneToOneField(
        SecretIdentity,
        on_delete=models.CASCADE,
        related_name='hero',
        null=True,
    )


class Sidekick(models.Model):

    id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        primary_key=True
    )
    name = models.CharField(
        max_length=100,
        blank=False
    )
    secret_identity = models.OneToOneField(
        SecretIdentity,
        on_delete=models.CASCADE,
        related_name='sidekick',
        null=True,
    )
    hero = models.ForeignKey(
        Hero,
        on_delete=models.DO_NOTHING,
        related_name='sidekicks'
    )


class Villain(models.Model):

    id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        primary_key=True
    )
    name = models.CharField(
        max_length=100,
        blank=False
    )
    archenemy = models.OneToOneField(
        Hero,
        on_delete=models.DO_NOTHING,
        related_name='archenemy',
        null=True
    )
