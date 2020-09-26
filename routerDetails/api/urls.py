
from rest_framework.routers import DefaultRouter

from routerDetails.api.views import RouterDetailViewSet

router = DefaultRouter()
router.register(r'', RouterDetailViewSet )

urlpatterns = router.urls