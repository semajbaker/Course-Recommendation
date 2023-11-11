from django.urls import path
from . import views
urlpatterns = [
    path('', views.recommend_courses, name='recommend_courses'),
]
