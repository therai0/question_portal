from django.urls import path
from .views import Homepage_logo_view
urlpatterns = [
    path('logos/',Homepage_logo_view.as_view(),name='logo_view')
]
