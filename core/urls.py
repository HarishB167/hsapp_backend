from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('apps', views.AppViewSet, basename='apps')

urlpatterns = router.urls 

