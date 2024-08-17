from django.db import models

# Create your models here.

class NewsModel(models.Model):
    image_name = models.CharField(
        blank=False,
        max_length=255
    )
    news_title = models.CharField(
        blank=False,
        null=False,
        max_length=255
        )
    description = models.TextField(
        blank=False,
        null=False,
    )
    publish_date = models.DateField(
        blank=False,
        null=False
    )