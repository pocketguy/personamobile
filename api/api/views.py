from rest_framework import viewsets

from .models import Factory, File, Post, Project
from .permissions import IsAdminUserOrReadOnly
from .serializers import (
    FactorySerializer,
    FileSerializer,
    PostSerializer,
    ProjectSerializer,
)

from django.utils.timezone import now


class FileViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUserOrReadOnly]
    queryset = File.objects.all()
    serializer_class = FileSerializer


class FactoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUserOrReadOnly]
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer
    lookup_field = "slug"


class ProjectViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUserOrReadOnly]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = "slug"


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUserOrReadOnly]
    queryset = Post.objects.filter(
        published=True, published_at__gte=now()
    ).order_by("-published_at")
    serializer_class = PostSerializer
    lookup_field = "slug"
