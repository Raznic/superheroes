# Generated by Django 2.1.4 on 2018-12-15 14:53

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('secret_identity', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='characters.Character')),
            ],
        ),
        migrations.CreateModel(
            name='Sidekick',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('hero', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='sidekicks', to='characters.Hero')),
                ('secret_identity', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='characters.Character')),
            ],
        ),
        migrations.CreateModel(
            name='Villain',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('archenemy', models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='archenemy', to='characters.Hero')),
            ],
        ),
    ]