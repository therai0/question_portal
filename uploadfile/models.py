from django.db import models
from django.core.validators import (
    FileExtensionValidator,
    MinValueValidator,
    MaxValueValidator,
)


# Create your models here.
class UploadFile(models.Model):

    bit = "BIT"
    bhm = "BHM"
    bba = "BBA"
    mba = "MBA"

    faculty_types = [
        (bit, "BIT"),
        (bhm, "BHM"),
        (bba, "BBA"),
        (mba, "MBA"),
    ]

    subject = models.CharField(max_length=255, blank=False, null=False)
    file = models.FileField(
        upload_to="pdf/",
        blank=False,
        null=False,
        validators=[FileExtensionValidator(["pdf"])],
    )

    years = models.CharField(max_length=255, blank=False, null=False)
    semester = models.IntegerField(
        blank=False,
        null=False,
        validators=[MinValueValidator(1), MaxValueValidator(8)],
        help_text="Invalid semester",
    )
    faculty = models.CharField(
        choices=faculty_types,
        blank=False,
        max_length=255,
        null=False)
    description = models.TextField(
        blank=False,
        null=False,
        default="Click the download bottom and download the question"
    )
