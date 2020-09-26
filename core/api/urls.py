
from rest_framework import routers

from core.api.views import    LoginViewSet, LogoutViewSet, RouterDetailAuthViewSet

router = routers.DefaultRouter()
# router.register('user', userviewsets )
router.register('login', LoginViewSet , basename='login')
router.register('logout', LogoutViewSet , basename='logout')
router.register( 'router-auth' ,RouterDetailAuthViewSet)
# router.register( 'router-filter', RouterFilterList)
urlpatterns = router.urls
