from django.urls import path
from main import views

urlpatterns = [
    path("", views.main_page, name="home"),
]