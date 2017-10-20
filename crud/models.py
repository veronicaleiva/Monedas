from django.db import models

# Create your models here.
class Monedas(models.Model):
    '''
    modelo de datos que crea tabla de Monedas
    '''
    nombre      = models.CharField(max_length= 30) # atributo nombre, es obligatorio
    abreviacion = models.CharField(max_length= 3, blank=False, unique=True)

    def __str__(self):
        return self.nombre

class Paridades(models.Model):
    '''
    detalle de la tabla de Monedas
    '''
    moneda  = models.ForeignKey(Monedas)
    fecha   = models.DateField()
    Paridad = models.DecimalField(max_digits=10, decimal_places=4)

    def __str__(self):
        return str(self.moneda) +'-' + str(self.fecha)
