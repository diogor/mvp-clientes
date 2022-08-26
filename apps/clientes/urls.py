from rest_framework import routers
from .views import ClienteViewSet


router = routers.DefaultRouter()

router.register(r"", ClienteViewSet)

urlpatterns = router.urls
