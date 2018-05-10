from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Precios(models.Model):
	nombreprenda = models.CharField(max_length=400)
	precio = models.DecimalField(max_digits=200,decimal_places=2)

	def __unicode__(self):
		return u'%s' % (self.nombreprenda)

class Registro(models.Model):
	nombre = models.CharField(max_length=400)
	email = models.CharField(max_length=400)
	mensaje = models.CharField(max_length=400)

	def __unicode__(self):
		return u'%s' % (self.nombre)