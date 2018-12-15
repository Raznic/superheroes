from django.test import TestCase

from . import models, serializers


class HeroModelTestCase(TestCase):
    fixtures = ['characters', 'heroes', 'sidekicks', 'villains']

    def test_batman_secret_identity(self):
        """
        Test that Batman has a secret identity
        """
        batman = models.Hero.objects.get(name='Batman')
        self.assertIsNotNone(batman.secret_identity)
        self.assertEqual("Bruce Wayne", batman.secret_identity.name)

    def test_batman_sidekicks(self):
        """
        Test that Batman always has the Boy Wonder by his side
        """
        batman = models.Hero.objects.get(name='Batman')
        sidekicks = batman.sidekicks.all()
        self.assertEqual(4, len(sidekicks))
        self.assertListEqual(['Robin', 'Robin', 'Robin', 'Robin'], list(map(lambda x: x.name, sidekicks)))

    def test_batman_archenemy(self):
        """
        Test that Batman is always fighting the Clown Prince of Crime
        """
        batman = models.Hero.objects.get(name='Batman')
        self.assertIsNotNone(batman.archenemy)
        self.assertEqual("The Joker", batman.archenemy.name)


class HeroSerializerTestCase(TestCase):

    def test_create_hero(self):
        self.assertEqual(0, len(models.Hero.objects.all()))
        serializer = serializers.HeroSerializer(
            data={
                'name': 'Moon Knight'
            }
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        self.assertEqual(1, len(models.Hero.objects.all()))

    def test_update_hero(self):
        hero = models.Hero.objects.create(
            name='Spider-Man'
        )
        character = models.Character.objects.create(
            name='Peter Parker'
        )
        self.assertIsNone(hero.secret_identity)
        serializer = serializers.HeroSerializer(
            hero,
            data={
                'secret_identity': character.id
            },
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        hero.refresh_from_db()
        self.assertEqual(character, hero.secret_identity)

    def test_blank_name(self):
        """
        Test that a Hero must have a name
        """
        serializer = serializers.HeroSerializer(
            data={
                'name': ''
            }
        )
        serializer.is_valid()
        self.assertIsNotNone(serializer.errors.get('name'))
        self.assertListEqual(
            [
                'This field may not be blank.'
            ],
            serializer.errors['name']
        )

    def test_null_name(self):
        """
        Test that a Hero must have a name
        """
        serializer = serializers.HeroSerializer(
            data={
                'name': None,
            }
        )
        serializer.is_valid()
        self.assertIsNotNone(serializer.errors.get('name'))
        self.assertListEqual(
            [
                'This field may not be null.'
            ],
            serializer.errors['name']
        )
