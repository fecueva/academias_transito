# Create your models here.
from __future__ import unicode_literals

from django.db import models


class Clasevehiculo(models.Model):
    descripcion = models.CharField(max_length=60, blank=True, null=True)
    idclasev = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'clasevehiculo'


class Combustibles(models.Model):
    nombrecomb = models.CharField(max_length=60, blank=True, null=True)
    idcomb = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'combustibles'


class Provincias(models.Model):
    nombreprov = models.CharField(max_length=60, blank=True, null=True)
    idprov = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'provincias'


class Tipovehiculo(models.Model):
    nombretipov = models.CharField(max_length=60, blank=True, null=True)
    idtipov = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'tipovehiculo'


class Vehiculos(models.Model):
    placa = models.CharField(max_length=15, blank=True, null=True)
    modelo = models.CharField(max_length=6, blank=True, null=True)
    marca = models.CharField(max_length=30, blank=True, null=True)
    tonelaje = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    asientos = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    idtipov = models.ForeignKey(Tipovehiculo, db_column='idtipov', blank=True, null=True)
    idclasev = models.ForeignKey(Clasevehiculo, db_column='idclasev', blank=True, null=True)
    idcomb = models.ForeignKey(Combustibles, db_column='idcomb', blank=True, null=True)
    idprov = models.ForeignKey(Provincias, db_column='idprov', blank=True, null=True)
    idvehiculo = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'vehiculos'
    def __unicode__(self):
	return "%s - %s - %s" % (self.placa, self.modelo, self.idtipov.nombretipov)


