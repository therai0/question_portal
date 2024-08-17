from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils.timezone import now

# Create your models here.

class BlogModel(models.Model):

    technology = "Techonology"
    economy = "Economy"
    programming = "Programming"
    hacking = "Hacking"
    politics = "Politics"
    sports = "Sports"
    esport = "Esport"
    others = "Others"


    blog_types = [
        (technology,"Technology"),
        (programming,"Programming"),
        (economy,"Economy"),
        (hacking,"Hacking"),
        (politics,"Politics"),
        (sports,"Sports"),
        (esport,"Esports"),
        (others,"Others")
    ]

    blog_title = models.CharField(
        null=False,
        blank=False,
        max_length=255
    )
    image_name = models.CharField(
        max_length=255,
        blank=False,
        null=False
        )
    blog_image = models.ImageField(
        validators=[FileExtensionValidator(['png','jpg'])],
        upload_to='blog/image/'
    )
    update_date = models.DateField(
        null=False,
        blank=False
    )
    blog_cetagory = models.CharField(
        max_length=255,
        choices=blog_types
    )
    blog_paragraph = models.TextField(
        blank=False,
        null=False,
        default=' '
    )

    