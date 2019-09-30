# import os
# import uuid

from ckeditor.fields import RichTextField
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.db import models
from django.utils.text import slugify

# def get_upload_to(instance, filename):
#     ext = filename.split(".")[-1]
#     name = uuid.uuid4().hex
#     filename = f"{name}.{ext}"
#     path = "uploads/"
#     return os.path.join(path, filename)


class File(models.Model):
    file = models.FileField(verbose_name="файл")  # upload_to=get_upload_to
    description = models.CharField(max_length=255, verbose_name="описание файла")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "файл"
        verbose_name_plural = "файлы"


class Factory(models.Model):
    name = models.CharField(max_length=255, verbose_name="название")
    description = models.TextField(verbose_name="описание")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=255, unique=True, editable=False)
    cover = models.ForeignKey(File, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "фабрика"
        verbose_name_plural = "фабрики"


class Project(models.Model):
    name = models.CharField(max_length=255, verbose_name="название")
    description = models.TextField(verbose_name="описание")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=255, unique=True, editable=False)
    cover = models.ForeignKey(File, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "проект"
        verbose_name_plural = "проекты"


class Post(models.Model):
    title = models.CharField(max_length=255)
    lead = models.TextField()
    text = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=255, unique=True, editable=False)
    cover = models.ForeignKey(File, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "новость"
        verbose_name_plural = "новости"
