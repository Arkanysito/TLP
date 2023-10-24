from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Entidad(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=40,default='')
    logo = models.ImageField()

class Comunicado(models.Model):
    TIPO_CHOICES=[("S","Suspension de actividades"),
                ("C","Suspension de clase"),
                ("I","Informacion"),
    ]
    
    id = models.BigAutoField(primary_key=True)
    titulo = models.CharField(max_length=60)
    detalle = models.TextField()
    detalle_corto =models.TextField()
    tipo = models.CharField(max_length=1,choices=TIPO_CHOICES)
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE)
    visible = models.BooleanField()
    fecha_publicacion = models.DateTimeField( auto_now_add=True)
    fecha_ultima_publicacion = models.DateField(auto_now=True)
    
    

    
    