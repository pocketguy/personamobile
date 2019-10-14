from rest_framework import serializers
from .models import File, Factory, Project, Post
from django.db.utils import IntegrityError


class FileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = File
        fields = ["id", "url", "file", "description", "created_at", "updated_at"]


class AutoSlugFieldModelSerializer(serializers.HyperlinkedModelSerializer):
    def create(self, *args, **kwargs):
        try:
            return super().create(*args, **kwargs)
        except IntegrityError as e:
            raise serializers.ValidationError(
                "object with this slug already exists"
            ) from e


class FactorySerializer(AutoSlugFieldModelSerializer):
    cover = FileSerializer(read_only=True)
    cover_id = serializers.PrimaryKeyRelatedField(
        queryset=File.objects.all(), source="cover", write_only=True
    )

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
            "cover_id",
        ]


class ProjectSerializer(AutoSlugFieldModelSerializer):
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


class PostSerializer(AutoSlugFieldModelSerializer):
    cover = FileSerializer()

    class Meta:
        model = Post
        lookup_field = "slug"
        extra_kwargs = {"url": {"lookup_field": "slug"}}
        fields = [
            "url",
            "title",
            "text",
            "seo_title",
            "seo_description",
            "created_at",
            "updated_at",
            "slug",
            "cover",
        ]
