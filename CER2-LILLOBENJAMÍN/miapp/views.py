from django.shortcuts import render
from django.http import HttpResponse
from .models import Entidad,Comunicado
# Create your views here.

def base(request):
    title = "Inicio"
    comunicados = Comunicado.objects.all()
    entidades=Entidad.objects.all()
    
    data = {
        "title": title,
        "comunicados":comunicados.order_by('-fecha_publicacion'),
        "entidades":entidades.order_by('-nombre'),

    }

    return render(request,'base.html/', data)