from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(AbstractUser):
    ROLES = [('ADMIN','Administrador'),('CLIENTE','Cliente')]
    rol = models.CharField(max_length=50,choices=ROLES,default='CLIENTE')


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos') # Relacionando Producto a una Categoria (Muchos a 1)

    def __str__(self):
        return self.nombre