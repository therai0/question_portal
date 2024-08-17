from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import Blog_views
urlpatterns = [
    path('blogs/',Blog_views.as_view(),name='blog_views')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
