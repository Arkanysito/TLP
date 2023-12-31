# Generated by Django 4.2.6 on 2023-10-24 08:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Entidad',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(default='', max_length=40)),
                ('logo', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Comunicado',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=60)),
                ('detalle', models.TextField()),
                ('detalle_corto', models.TextField()),
                ('tipo', models.CharField(choices=[('S', 'Suspension de actividades'), ('C', 'Suspension de clase'), ('I', 'Informacion')], max_length=1)),
                ('visible', models.BooleanField()),
                ('fecha_publicacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_ultima_publicacion', models.DateField(auto_now=True)),
                ('entidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='miapp.entidad')),
                ('modificado_por', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='modificado_por', to=settings.AUTH_USER_MODEL)),
                ('publicado_por', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
