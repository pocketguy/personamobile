from django.db import models
from django.utils.text import slugify

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
    slug = models.SlugField(
        max_length=255, unique=True, verbose_name="адрес", editable=False
    )

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name = "фабрика"
        verbose_name_plural = "фабрики"
