from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient

from . import models, serializers, filters


class HeroModelTestCase(TestCase):
    fixtures = ['secret_identities', 'heroes', 'sidekicks', 'villains']

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
                'name': 'Moon Knight',
            }
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        self.assertEqual(1, len(models.Hero.objects.all()))

    def test_update_hero(self):
        hero = models.Hero.objects.create(
            name='Spider-Man'
        )
        identity = models.SecretIdentity.objects.create(
            name='Peter Parker'
        )
        self.assertIsNone(hero.secret_identity)
        serializer = serializers.HeroSerializer(
            hero,
            data={
                'secret_identity_id': identity.id
            },
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        hero.refresh_from_db()
        self.assertEqual(identity, hero.secret_identity)

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


class HeroFilterSetTestCase(TestCase):
    fixtures = ['secret_identities', 'heroes', 'sidekicks', 'villains']

    def test_filter_name(self):
        filterset = filters.HeroFilterSet(
            data={
                'name': 'Batman'
            },
            queryset=models.Hero.objects.all()
        )
        self.assertEqual(1, len(filterset.qs))

    def test_filter_name_icontains(self):
        filterset = filters.HeroFilterSet(
            data={
                'name__icontains': 'Green'
            },
            queryset=models.Hero.objects.all()
        )
        self.assertEqual(2, len(filterset.qs))


class HeroViewSetTestCase(APITestCase):
    fixtures = ['secret_identities', 'heroes', 'sidekicks', 'villains']

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='test')

    def test_unauthenticated_list(self):
        response = self.client.get('/api/v1/heroes/')
        self.assertEqual(200, response.status_code)

    def test_unauthenticated_create(self):
        response = self.client.post(
            '/api/v1/heroes/',
            data={
                'name': 'The Question',
            }
        )
        self.assertEqual(401, response.status_code)

    def test_unauthenticated_retrieve(self):
        hero = models.Hero.objects.first()
        self.assertIsNotNone(hero)
        response = self.client.get(f'/api/v1/heroes/{hero.id}/')
        self.assertEqual(200, response.status_code)

    def test_unauthenticated_update(self):
        hero = models.Hero.objects.first()
        self.assertIsNotNone(hero)
        response = self.client.put(
            f'/api/v1/heroes/{hero.id}/',
            data={
                'name': hero.name,
                'secret_identity': hero.secret_identity.id,
            }
        )
        self.assertEqual(401, response.status_code)

    def test_unauthenticated_partial_update(self):
        hero = models.Hero.objects.first()
        self.assertIsNotNone(hero)
        response = self.client.patch(
            f'/api/v1/heroes/{hero.id}/',
            data={
                'name': hero.name,
                'secret_identity': hero.secret_identity.id,
            }
        )
        self.assertEqual(401, response.status_code)

    def test_unauthenticated_delete(self):
        hero = models.Hero.objects.first()
        self.assertIsNotNone(hero)
        response = self.client.delete(f'/api/v1/heroes/{hero.id}/')
        self.assertEqual(401, response.status_code)

    def test_authenticated_list(self):
        self.client.force_authenticate(self.user)
        response = self.client.get('/api/v1/heroes/')
        self.assertEqual(200, response.status_code)

    def test_authenticated_create(self):
        self.client.force_authenticate(self.user)
        response = self.client.post(
            '/api/v1/heroes/',
            data={
                'name': 'The Question'
            }
        )
        self.assertEqual(201, response.status_code)

    def test_authenticated_retrieve(self):
        hero = models.Hero.objects.first()
        self.assertIsNotNone(hero)
        self.client.force_authenticate(self.user)
        response = self.client.get(f'/api/v1/heroes/{hero.id}/')
        self.assertEqual(200, response.status_code)

    def test_authenticated_update(self):
        hero = models.Hero.objects.first()
        self.assertIsNotNone(hero)
        self.client.force_authenticate(self.user)
        response = self.client.put(
            f'/api/v1/heroes/{hero.id}/',
            data={
                'name': hero.name,
                'secret_identity': hero.secret_identity.id,
            }
        )
        self.assertEqual(200, response.status_code)

    def test_authenticated_partial_update(self):
        hero = models.Hero.objects.first()
        self.assertIsNotNone(hero)
        self.client.force_authenticate(self.user)
        response = self.client.patch(
            f'/api/v1/heroes/{hero.id}/',
            data={
                'name': hero.name,
                'secret_identity': hero.secret_identity.id,
            }
        )
        self.assertEqual(200, response.status_code)

    def test_authenticated_delete(self):
        hero = models.Hero.objects.first()
        self.assertIsNotNone(hero)
        self.client.force_authenticate(self.user)
        response = self.client.delete(f'/api/v1/heroes/{hero.id}/')
        self.assertEqual(204, response.status_code)


class SecretIdentityViewSetTestCase(APITestCase):
    fixtures = ['secret_identities', 'heroes', 'sidekicks', 'villains']

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='test')

    def test_unauthenticated_list(self):
        response = self.client.get('/api/v1/secret_identities/')
        self.assertEqual(401, response.status_code)

    def test_unauthenticated_create(self):
        response = self.client.post(
            '/api/v1/secret_identities/',
            data={
                'name': 'Matt Murdock',
            }
        )
        self.assertEqual(401, response.status_code)

    def test_unauthenticated_retrieve(self):
        identity = models.SecretIdentity.objects.first()
        self.assertIsNotNone(identity)
        response = self.client.get(f'/api/v1/secret_identities/{identity.id}/')
        self.assertEqual(401, response.status_code)

    def test_unauthenticated_update(self):
        identity = models.SecretIdentity.objects.first()
        self.assertIsNotNone(identity)
        response = self.client.put(
            f'/api/v1/secret_identities/{identity.id}/',
            data={
                'name': identity.name,
            }
        )
        self.assertEqual(401, response.status_code)

    def test_unauthenticated_partial_update(self):
        identity = models.SecretIdentity.objects.first()
        self.assertIsNotNone(identity)
        response = self.client.patch(
            f'/api/v1/secret_identities/{identity.id}/',
            data={
                'name': identity.name,
            }
        )
        self.assertEqual(401, response.status_code)

    def test_unauthenticated_delete(self):
        identity = models.SecretIdentity.objects.first()
        self.assertIsNotNone(identity)
        response = self.client.delete(f'/api/v1/secret_identities/{identity.id}/')
        self.assertEqual(401, response.status_code)

    def test_authenticated_list(self):
        self.client.force_authenticate(self.user)
        response = self.client.get('/api/v1/secret_identities/')
        self.assertEqual(200, response.status_code)

    def test_authenticated_create(self):
        self.client.force_authenticate(self.user)
        response = self.client.post(
            '/api/v1/secret_identities/',
            data={
                'name': 'Matt Murdock',
            }
        )
        self.assertEqual(201, response.status_code)

    def test_authenticated_retrieve(self):
        identity = models.SecretIdentity.objects.first()
        self.assertIsNotNone(identity)
        self.client.force_authenticate(self.user)
        response = self.client.get(f'/api/v1/secret_identities/{identity.id}/')
        self.assertEqual(200, response.status_code)

    def test_authenticated_update(self):
        identity = models.SecretIdentity.objects.first()
        self.assertIsNotNone(identity)
        self.client.force_authenticate(self.user)
        response = self.client.put(
            f'/api/v1/secret_identities/{identity.id}/',
            data={
                'name': identity.name,
            }
        )
        self.assertEqual(200, response.status_code)

    def test_authenticated_partial_update(self):
        identity = models.SecretIdentity.objects.first()
        self.assertIsNotNone(identity)
        self.client.force_authenticate(self.user)
        response = self.client.patch(
            f'/api/v1/secret_identities/{identity.id}/',
            data={
                'name': identity.name,
            }
        )
        self.assertEqual(200, response.status_code)

    def test_authenticated_delete(self):
        identity = models.SecretIdentity.objects.first()
        self.assertIsNotNone(identity)
        self.client.force_authenticate(self.user)
        response = self.client.delete(f'/api/v1/secret_identities/{identity.id}/')
        self.assertEqual(204, response.status_code)
