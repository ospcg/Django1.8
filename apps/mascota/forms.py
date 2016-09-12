from django import forms
from apps.mascota.models import Mascota

class MascotaForm(forms.ModelForm):

	class Meta:
		model = Mascota
		#tupla que contiene los campos del modelo mascota
		fields = [
			'nombre',
			'sexo',
			'edad_aproximada',
			'fecha_rescate',
			'persona',
			'vacuna',

		]
		#diccionario con el nombre que va a llevar cada campo
		labels = {
			'nombre' :'Nombre',
			'sexo' : 'Sexo',
			'edad_aproximada' : 'Edad Aproximada',
			'fecha_rescate' : 'Fecha de rescate',
			'persona' : 'Adoptante',
			'vacuna' : 'Vacuna',
		}
		#diccionario con el diseno de cada campo para ingresar cada dato
		widgets = {
			'nombre': forms.TextInput(attrs = {'class':'form-control'}),
			'sexo': forms.TextInput(attrs = {'class':'form-control'}),
			'edad_aproximada': forms.TextInput(attrs = {'class':'form-control'}),
			'fecha_rescate': forms.TextInput(attrs = {'class':'form-control'}),
			'persona': forms.Select(attrs = {'class':'form-control'}),
			'vacuna': forms.CheckboxSelectMultiple(),

		}