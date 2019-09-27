from django.db import models

# class Media(models.Model):
#     file = models.FileField("")
#     name = models.CharField("")

#     class Meta:
#         verbose_name = "медиа"
#         verbose_name_plural = "медиа"


class Factory(models.Model):
    name = models.CharField(max_length=255, verbose_name="название")
    description = models.TextField(verbose_name="описание")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=255, unique=True, verbose_name="адрес")

    class Meta:
        verbose_name = "фабрика"
        verbose_name_plural = "фабрики"
