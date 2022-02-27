from rest_framework.routers import DefaultRouter

from team.views import TeamViewset

router = DefaultRouter()
router.register(r'teams', TeamViewset, basename='teams')

urlpatterns = router.urls