from rest_framework import routers

from .views import FileViewSet, FactoryViewSet, ProjectViewSet, PostViewSet

router = routers.DefaultRouter()
router.register("files", FileViewSet)
router.register("factories", FactoryViewSet)
router.register("projects", ProjectViewSet)
router.register("posts", PostViewSet, base_name='post')
