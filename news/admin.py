from django.contrib import admin

# Register your models here.
from .models import NewsModel
admin.site.register(NewsModel)