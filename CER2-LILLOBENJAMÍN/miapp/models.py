from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Entidad(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=40,default='')
    logo = models.ImageField()
    def __str__(self) -> str:
        return self.nombre

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
    publicado_por=models.ForeignKey(User, on_delete=models.CASCADE, editable=False, null=True)
    modificado_por=models.ForeignKey(User, related_name="modificado_por", on_delete=models.CASCADE, editable=False, null=True)
    def __str__(self) -> str:
        return self.titulo

    
    