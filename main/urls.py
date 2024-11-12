from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("main/", views.main_view, name="main"),
    path("login/", views.custom_login, name="login"),
    path("vehiculos/", views.vehiculos_view, name="vehiculos"),
    path("combustibles/", views.combustibles_view, name="combustibles"),
    path("calculos/", views.calculos_view, name="calculos"),
    path("logout/", include("django.contrib.auth.urls")),
]
