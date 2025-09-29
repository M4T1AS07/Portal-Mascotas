from django.contrib import admin
from .models import Mascota, SolicitudAdopcion, Post


@admin.register(Mascota)
class MascotaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "especie", "edad")
    search_fields = ("nombre", "especie")


@admin.register(SolicitudAdopcion)
class SolicitudAdopcionAdmin(admin.ModelAdmin):
    list_display = ("nombre_completo", "email", "telefono", "get_mascota", "fecha")
    list_filter = ("fecha",)
    search_fields = ("nombre_completo", "email", "telefono", "mascota__nombre")

    def get_mascota(self, obj):
        return obj.mascota.nombre
    get_mascota.short_description = "Mascota"


admin.site.register(Post)