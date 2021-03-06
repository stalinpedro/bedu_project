from django.db import models


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=80, null=True, blank=True)
    email = models.EmailField()
    birthday = models.DateField(null=True, blank=True)

    GENERO = [("H", "Hombre"), ("M", "Mujer")]
    genre = models.CharField(max_length=1, choices=GENERO)
    key = models.CharField(max_length=40, null=True, blank=True)
    type = models.CharField(max_length=45, null=True, blank=True)

    def __str__(self):
        return "{} {}".format(self.name, self.last_name)


class Zone(models.Model):
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=256, null=True, blank=True)
    latitud = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True)

    def __str__(self):
        return "{}".format(self.name)


class Tour(models.Model):
    """ Define la tabla Tour """
    nombre = models.CharField(max_length=145)
    slug = models.CharField(max_length=45, null=True, blank=True)
    operador = models.CharField(max_length=45, null=True, blank=True)
    tipoDeTour = models.CharField(max_length=45, null=True, blank=True)
    descripcion = models.CharField(max_length=256)
    img = models.CharField(max_length=256, null=True, blank=True)
    pais = models.CharField(max_length=45, null=True, blank=True)
    zonaSalida = models.ForeignKey(Zone, on_delete=models.SET_NULL, null=True,
                                   blank=True, related_name="tours_salida")
    zonaLlegada = models.ForeignKey(Zone, on_delete=models.SET_NULL, null=True,
                                    blank=True, related_name="tours_llegada")

    def __str__(self):
        return "{}".format(self.nombre)
