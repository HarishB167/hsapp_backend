from django.urls import path
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('mindmaps', views.MindmapViewSet, basename='mindmaps')

mindmaps_router = routers.NestedDefaultRouter(router, 'mindmaps', lookup='mindmap')
mindmaps_router.register('branches', views.BranchViewSet, basename='mindmap-branch')

branches_router = routers.NestedDefaultRouter(mindmaps_router, 'branches', lookup='branch')
branches_router.register('branchline', views.BranchLineViewSet, basename='mindmap-branches-branchline')

urlpatterns = router.urls + mindmaps_router.urls + branches_router.urls

