from django.db import models
from django.contrib.auth.models import User



class Empresa(models.Model):
    nombre = models.CharField(max_length=200, null=True)
    facultad = models.CharField(max_length=200, null=True)


class Solicitud(models.Model):
    estado = models.CharField(max_length=10, null=True)

    usuario = models.ForeignKey(
        User,
        related_name='solicitudes',
        on_delete=models.PROTECT
    )
    empresa = models.ForeignKey(
        Empresa,
        related_name='solicitudes',
        on_delete=models.PROTECT
    )
    def __str__(self):
        return self.estado

    class Meta:
        app_label = 'pasantias'



