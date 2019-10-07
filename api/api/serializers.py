from rest_framework import serializers
from .models import File, Factory, Project, Post


class FileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = File
        fields = ["id", "url", "file", "description", "created_at", "updated_at"]


class FactorySerializer(serializers.HyperlinkedModelSerializer):
    cover = FileSerializer()

    class Meta:
        model = Factory
        lookup_field = "slug"
        extra_kwargs = {"url": {"lookup_field": "slug"}}
        fields = [
            "url",
            "name",
            "description",
            "created_at",
            "updated_at",
            "slug",
            "cover",
        ]


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    cover = FileSerializer()

    class Meta:
        model = Project
        lookup_field = "slug"
        extra_kwargs = {"url": {"lookup_field": "slug"}}
        fields = [
            "url",
            "name",
            "description",
            "created_at",
            "updated_at",
            "slug",
            "cover",
        ]


class PostSerializer(serializers.HyperlinkedModelSerializer):
    cover = FileSerializer()

    class Meta:
        model = Post
        lookup_field = "slug"
        extra_kwargs = {"url": {"lookup_field": "slug"}}
        fields = [
            "url",
            "title",
            "lead",
            "text",
            "created_at",
            "updated_at",
            "slug",
            "cover",
        ]