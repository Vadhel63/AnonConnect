from django.urls import path
from . import views
urlpatterns = [
    path('anon/',views.about,name="about"),
]