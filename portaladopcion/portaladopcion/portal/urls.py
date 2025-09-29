from django.urls import path
from . import views

app_name = "portal"   # 👈 importante

urlpatterns = [
    path("", views.home, name="home"),
    path("mascotas/", views.lista_mascotas, name="lista_mascotas"),
    path("mascotas/<int:mascota_id>/adoptar/", views.solicitar_adopcion, name="solicitar_adopcion"),
    path("blog/", views.blog, name="blog"),
]
