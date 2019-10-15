# import os
# import uuid

import os
import uuid

from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.text import slugify
from django.utils.timezone import now


def get_filename(filename):
    ext = filename.split(".")[-1]
    name = uuid.uuid4().hex
    filename = f"{name}.{ext}"
    return filename


def get_upload_to(instance, filename):
    filename = get_filename(filename)
    path = "uploads/"
    return os.path.join(path, filename)


class File(models.Model):
    file = models.FileField(verbose_name="файл", upload_to="media/")
    description = models.CharField(max_length=255, verbose_name="описание файла")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "файл"
        verbose_name_plural = "файлы"
        ordering = ["created_at"]


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
        ordering = ["created_at"]


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
        ordering = ["created_at"]


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок", blank=True)
    text = RichTextUploadingField(verbose_name="Основной текст")
    cover = models.ForeignKey(File, on_delete=models.CASCADE, verbose_name="Обложка")
    published = models.BooleanField(
        verbose_name="Опубликован",
        default=False
    )
    published_at = models.DateTimeField(
        verbose_name="Дата публикации",
        help_text="Может быть в будущем (будет отложенная публикация)",
        default=now,
    )
    seo_title = models.CharField(
        max_length=255, verbose_name="(SEO) Заголовок", blank=True
    )
    seo_description = models.TextField(verbose_name="(SEO) Описание")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=255, unique=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "новость"
        verbose_name_plural = "новости"
        ordering = ["created_at"]
