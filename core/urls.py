from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('apps', views.AppViewSet, basename='apps')
router.register('contactmessage', views.ContactMessageViewSet, basename='contactmessage')

urlpatterns = router.urls 

