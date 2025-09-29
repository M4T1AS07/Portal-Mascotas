from django.db import models

class Blog(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo


class Mascota(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre de la mascota")
    especie = models.CharField(max_length=50, verbose_name="Especie", help_text="Ej: perro, gato")
    edad = models.PositiveIntegerField(verbose_name="Edad (años)")
    descripcion = models.TextField(blank=True)
    imagen = models.ImageField(upload_to="mascotas/", blank=True, null=True)
    solicitudadopcion = models.BooleanField(default=False)
    disponible = models.BooleanField(default=True)
    ubicacion = models.CharField(max_length=100, default="Sin especificar")

def __str__(self):
    return f"{self.nombre} ({self.especie}, {self.edad} años)"



class SolicitudAdopcion(models.Model):
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE, related_name='solicitudes')
    nombre_completo = models.CharField(max_length=150)
    email = models.EmailField(default="correo@ejemplo.com")
    telefono = models.CharField(max_length=20)
    direccion = models.TextField()
    motivo = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Solicitud de {self.nombre_completo} para {self.mascota.nombre}"


class Post(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
