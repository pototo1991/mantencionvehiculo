from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("main/", views.main_view, name="main"),
    path(
        "login/", views.custom_login, name="login"
    ),  # Vista personalizada de inicio de sesión
]
