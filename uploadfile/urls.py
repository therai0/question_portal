
from django.urls import path
from .views import Question_views

urlpatterns = [
    path('questions/',Question_views.as_view(),name='question_views')
]
