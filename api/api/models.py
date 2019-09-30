import os
import uuid

from django.db import models
from django.utils.text import slugify


def get_upload_to(instance, filename):
    ext = filename.split(".")[-1]
    name = uuid.uuid4().hex
    filename = f"{name}.{ext}"
    path = "uploads/"
    return os.path.join(path, filename)


class File(models.Model):
    file = models.FileField(verbose_name="файл", upload_to=get_upload_to)
    description = models.CharField(max_length=255, verbose_name="описание файла")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.file.name

    class Meta:
        verbose_name = "файл"
        verbose_name_plural = "файлы"


class Factory(models.Model):
    name = models.CharField(max_length=255, verbose_name="название")
    description = models.TextField(verbose_name="описание")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(
        max_length=255, unique=True, verbose_name="адрес", editable=False
    )
    cover = models.ForeignKey(File, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name = "фабрика"
        verbose_name_plural = "фабрики"
