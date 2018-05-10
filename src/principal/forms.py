from django import forms
from .models import Precios, Registro
from django.forms import ModelForm, TextInput, DateField, NumberInput, SelectDateWidget


class PreciosForm(forms.ModelForm):
	class Meta:
		model = Precios
		fields = [
			'nombreprenda',
			'precio',
			
		]
		labels = {
			'nombreprenda': 'Nombre de la prenda',
			'precio' : 'Precio',
			

		}
		widgets = {
			'nombreprenda': forms.TextInput(attrs={'class':'form-control'}),
			'precio': forms.TextInput(attrs={'class':'form-control'}),
			
		}

class Registroform(forms.ModelForm):
	class Meta:
		model = Registro
		fields = [
			'nombre',
			'email',
			'mensaje',
			
		]
		labels = {
			'nombre': 'Nombre',
			'email' : 'Correo',
			'mensaje' : 'Mensaje',
			

		}
		widgets = {
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'email': forms.TextInput(attrs={'class':'form-control'}),
			'mensaje': forms.Textarea(attrs={'class':'form-control'}),
			
		}