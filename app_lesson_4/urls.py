from django.urls import path
from .views import home_work

urlpatterns = [
    path("lesson_4", home_work)
]