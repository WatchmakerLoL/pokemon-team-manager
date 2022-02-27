from rest_framework.routers import DefaultRouter

from trainer.views import TrainerViewset

router = DefaultRouter()
router.register(r'trainers', TrainerViewset, basename='trainers')

urlpatterns = router.urls
