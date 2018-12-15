from django.test import TestCase
from . import models


class HeroTestCase(TestCase):
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
