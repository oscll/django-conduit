from django.db import models
from conduit.apps.core.models import TimestampedModel
# Create your models here.


class Local(TimestampedModel):

    nombre= models.CharField(max_length=25)
    telefono= models.CharField(max_length=25)
    direccion= models.CharField(max_length=55)
    poblacion= models.CharField(max_length=25)
    provincia= models.CharField(max_length=25)
    latitud= models.CharField(max_length=255)
    longitud= models.CharField(max_length=255) 
    foto= models.CharField(max_length=255, blank=True) 
    categoria= models.CharField(max_length=25)
    author = models.ForeignKey(
        'profiles.Profile', related_name='locales', on_delete=models.CASCADE
    )

    def __str__(self):
        return self.nombre


class Comment(TimestampedModel):
    body = models.TextField()
    
    local = models.ForeignKey(
        'locales.Local', related_name='comments', on_delete=models.CASCADE
    )

    author = models.ForeignKey(
        'profiles.Profile', related_name='comments', on_delete=models.CASCADE
    )


class Producto(TimestampedModel):
    nombre = models.CharField(max_length=30)
    foto = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    price = models.FloatField()
    local = models.ForeignKey( 'locales.Local', related_name='producto', on_delete=models.CASCADE) 