from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.

# models for logo
class HomePage_logo(models.Model):
    logo_name = models.CharField(
        blank=False,
        null=False,
        max_length=255
    )
    logo = models.ImageField(
        blank=False,
        null=False,
        validators=[FileExtensionValidator(['jpg','png'])],
        upload_to='logo/'
    )



