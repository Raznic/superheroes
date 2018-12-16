from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register(r'secret_identities', views.SecretIdentityViewSet)
router.register(r'heroes', views.HeroViewSet)
router.register(r'sidekicks', views.SidekickViewSet)
router.register(r'villains', views.VillainViewSet)

app_name = 'characters'
urlpatterns = router.urls
